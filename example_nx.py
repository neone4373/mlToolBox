import networkx 


#Creating a graph
g = networkx.Graph()
g = networkx.Graph()
g.add_node("John")
g.add_node("Maria")
g.add_node("Alex")
g.add_edge("John", "Alex")
g.add_edge("Maria", "Alex")

print g.number_of_nodes()
print g.number_of_edges()

print g.nodes()
print g.edges()

print g.degree("John")
print g.degree()


#Creating a directed graph

g = networkx.DiGraph()
g.add_edges_from([("A","B"), ("C","A")])
#print g.in_degree(with_labels=True)
print g.in_degree()
print g.out_degree()
print g.neighbors("A")

ug = g.to_undirected()
print ug.neighbors("B")


#loading existing data

g = networkx.read_edgelist("./networkData/test.edgelist")
print g.edges()

g = networkx.read_adjlist("./networkData/test.adj")
print g.edges()


#weighted graphs

g = networkx.Graph()
g.add_edge("conor@deri.org", "anne@ucd.ie", weight=5)
g.add_edge("conor@deri.org", "mark@yahoo.ie", weight=2)
g.add_edge("conor@deri.org", "maria@gmail.com", weight=4)
g.add_edge("mark@yahoo.ie", "maria@gmail.com", weight=3)

#this causes estrong to only be populated with the nodes with weight > 3
estrong = [(u,v) for (u,v,d) in g.edges(data=True) if d["weight"] > 3]
print estrong

print g.degree("conor@deri.org", weighted=False)

print g.degree("conor@deri.org", weighted=True)


#Attribute graphs

g = networkx.Graph()
g.add_node("318064061", screen_name="peter78", location="Galway", time_zone="GMT")
g.add_node("317756843", screen_name="mark763", location="London", time_zone="GMT")

#And modifying attributes can be done on the fly
g.node["318064061"]["verified"] = False
g.node["317756843"]["verified"] = False

#Edges can also have attribute values
g.add_edge("318064061", "317756843", follow_date=datetime.datetime.now())



