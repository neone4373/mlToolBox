import psycopg2 as pg
import networkx as nx

post = { "DB" : 'postgres',
  "User" : 'pybot',
  "Pass": 'pybot',
  "Host": 'localhost',
  "Port": 5432}

# Connect to an existing database
conn = pg.connect("dbname=" + post["DB"] + " user=" + post["User"] + " password=" + post["Pass"])

# Open a cursor to perform database operations
cur = conn.cursor()


# Query the database and obtain data as Python objects

#users for nodes
cur.execute("SELECT * FROM twitter.users limit 100;")
users = cur.fetchall()
name_tup = []
for user in users:

  name_tup += [(user[3] , int(user[0]) , user[1])]

#tweets for edges
cur.execute("SELECT * FROM twitter.tweets limit 50000;")
tweets = cur.fetchall()
twit_lst = []
twit_dct = {}
name_dct = {}
for tweet in tweets:
  tt = (int(tweet[1]),tweet[9])
  if (tweet[11] != None and tt not in twit_dct):
    twit_dct[tt] = 1
    name_dct[tweet[9]] = tweet[11]
  elif (tweet[11] != None and tt in twit_dct):
    twit_dct[tt] += 1
  else:
    pass

inter_count = 0
for pairs in twit_dct.items():
  inter_count += pairs[1]
#print "Count of user pairs %s count of one way tweets %s" % (len(twit_dct),inter_count)
# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close() 
conn.close()
#initializes the graph
g = nx.DiGraph()

#adds in all the user nodes scrapped directly from twitter
for name in name_tup:
  g.add_node(name[1], handle=name[0], source = "as a user")

for t in twit_dct.items():
  g.add_edge(t[0][0],t[0][1], weight = t[1])

#adds the user data for nodes pulled in from tweets
for no in g.nodes():
  if (g.node[no] == {} and no in name_dct):
    g.node[no]["source"] = "as a tweet"
    g.node[no]["handle"] = name_dct[no]
  elif (g.node[no] == {} and no not in name_dct):
    g.node[no]["source"] = "as a phantom tweet"
  else:
    pass

#adding the in and out degree to see who is a big deal
for no in g.nodes():
    g.node[no]["in_degree"] = g.in_degree(no)
    g.node[no]["out_degree"] = g.out_degree(no)
gn = g.nodes(data=True)
ge = g.edges(data=True)

print "%s nodes with %s edges added to the graph" % (g.number_of_nodes(),g.number_of_edges())
print "\n  these guys are kind of a big deal"

bigDeal =  [(u,v) for (u,v) in gn if v["in_degree"] > 5  ]
posers  =  [(u,v) for (u,v) in gn if v["out_degree"] > 30 ]
print len(bigDeal)
for b in  bigDeal[:10]:
  print b
print "\n  these guys not so much"
print len(posers)
for p in posers[:10]:
  print p
