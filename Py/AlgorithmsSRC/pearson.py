#Pearson's Correlation Coeffcient
def pearson(x,y):
	n=len(x)
	vals=range(n)
#Simple Sums
	sumx=sum([float ([i]) for i in vals])
	sumy=sum([float ([i]) for i in vals])
#Sum up SQ
	sumxSq=sum([x[i]**2.0 for i in vals])
	sumySq=sum([y[i]**2.0 for i in vals])
#Sum Up Products
	pSums=sum([x[i]*y[i] for i in vals])
#Calculate Pearson
	num=pSum-(sumx*sumy/n)
	den=((sumxSq-pow(sumx,2/n)*(sumySq-pow(sumy,2/n))**.5
	if den==0: return 1
	r=num/den
	return r
	
	
# Real time Example
# Returns the Pearson Correlation Coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
  # Get the list of mutually rated items
  si={}
  for items in prefs[p1]:
    if items in prefs[p2]: si[item]=1
	
  # Find the number of elements
  n=len(si)
  
  # If they have no ratings in common, return 0
  if n==0: return 0
  
  # Add up all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  
  # Sum up the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
  
  # Sum up the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  
  # Calculate Pearson score
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
  
  r=num/den
  
  return r
  
Adding this function gets an ordered list of site users with similar interests to a specific user in order to make advertisement suggestions once implemented it will be automatic to the user.
 
# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity functions are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other)
                  for other in prefs if other!=person]
				   
  # Sort the list so the highest scores appear at the top
  scores.sort()
  scores.reverse()
  return scores[0:n]

This function will give you a data set to determine similarity of users that liked a particular item and mathcing products to them of other things they woyld like.

def transformPrefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
	  result.setdefault(item,{})
	  
	  # Flip item and person
	  result[item][person]=prefs[person][item]
   return result
   
Then we call our functions to execute.

>> from analytics import users
>> reload(analytics)
>> results=analytics.transformPrefs(analytics.users)
>> analytics.topMatches(links,online-shopping,ratings)