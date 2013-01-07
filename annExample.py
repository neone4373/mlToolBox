import scikits.ann as ann
#A library of ANN based off of the C++ library of the same name 
# this library is best used for calculating the nearest(x) 
# neighbors of a point to a non-constructed array of points
import numpy as np, random as r,math as m, pylab as mat
import scipy.stats as stat
tree = np.array([[0.,0],[1,0],[1.5,2]])


def randTree(N = 5, ind = 0, dim = 2, m = [0,0], s = [1,1]):
  #Creates a random tree length N, category ind, 
  #dimension dim, dimension mean m, dimension std s
  tree = np.empty((N,dim+1))
  for i in range(N):
    for j in range(dim):
      tree[i][j] = r.gauss(m[j],s[j])
    tree[i][dim] = int(ind)
  return tree

def randPoints(N = 1, dim = 2, m = [0,0], s = [1,1]):
  #Creates random points length (N), category (ind), 
  #dimension (dim), dimension mean (m), dimension std (s)
  points = np.empty((N,dim+1))
  for i in range(N):
    for j in range(dim):
      points[i][j] = r.gauss(m[j],s[j])
    points[i][dim] = 9999
  return points

def assignGroup(p,a):
  #Once the predications (a) for the points (p) are 
  # calculated this assigns them
  i = 0
  q = p
  while i < a.shape[0]:
    q[i][-1] = a[i]
    i += 1
  return q

def distGroups(tt):
  #Returns the distinct groups in your tree (tt)
  ff = []; 
  for a in tt[:,-1]: 
    if  a not in ff: 
      ff += [a]
  return ff

def predictedGroup(p, tr, nn = 3, e='s'):
  #Compares the points (p) to your tree (tr), providing its predicted 
  # category for each point based off of its (nn) nearest neighbors
  #Explaination can be short e[s] or long e[l]
  k = ann.kdtree(tr[:,:tr.shape[1]-1])
  l = k.knn(p[:,:p.shape[1]-1],3)
  #   dist = distGroups(tr)
  #   pr = []
  print "l[0]"; print l[0], "\n"; 
  #   print dist; 
  #   print "tr[0][-1] \n",tr[0][-1]
  if e == 's':
    for i in l[0]:
      pass
  else:
    print tr,"\n"; print p,"\n";
    ll = np.zeros((l[0].shape[0],p.shape[1]))
    kk = 0
    for i in l[0]:
      ii = 0
      for j in i:
        ll[kk][ii] = tr[j][-1]
        ii += 1
      kk += 1
    print "Groups \n", ll; print "Modes \n",stat.mode(ll,1)
  pred = assignGroup(p,stat.mode(ll,1)[0])
  print pred
  return pred

def plotItOut(p,tr):
  #show the first 2 dimensions in a scatter plota
  colours = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow']
  props = dict( alpha=0.5, edgecolors='none' )
  pts = np.vstack((tr,p))
  gps = distGroups(pts)
  scatterPT = [] 
  for i in gps:
    color = colours[gps.index(i)]
    drop = []
    qq = 0
    for q in pts:
      if int(q[-1]) != i:
        drop += [qq]
      aa = np.delete(pts, drop, axis=0)  
      #print "i",i,'q',q,"qq",qq, "drop row?",int(q[-1]) != i, "rows in aa", aa.shape[0]; 
      qq += 1
    scatterPT.append(mat.scatter(aa[:,0], aa[:,1], c=color, s=75, marker='o', **props))
  mat.legend(scatterPT,gps)
  mat.show(scatterPT)    
  mat.close()

points = randPoints(3,2,[2,2],[5,5])
tree = np.vstack((randTree(100, 5,2,[15,8],[5,5]), randTree(100,17,2,[8,10],[5,5])))

#print tree[:,:tree.shape[1]-1],"\n";
#print points[:,:points.shape[1]-1],"\n"

plotItOut(points,tree)

plotItOut(predictedGroup(points, tree, 3, 'l'),tree)
#print assignGroup(points,np.array([[1.],[0.],[1.]]))


