############################################################################
#  Since everyone loves Bayes' Theorem I am going to play with it a        #
#   little bit and see if I cant do something with it.                     #
############################################################################

def bayes(l = False):
  print "          P(B|A)P(A) "
  print "P(A|B) = ------------"
  print "             P(B)    "

def bayesThm(pA,pB,pBA):
  #This function takes P(A) [pA], P(B) [pB], and P(B|A) [pBA] and
  #  returns P(A|B)
  if pB != 0:
    return float((pBA * pA) / pB)
  else:
    print "P(B) = 0 then P(A|B) does not exist because P(B) cannot happen"


print bayesThm(.5,(.6*.5+(4./7.)*.5),.6)
