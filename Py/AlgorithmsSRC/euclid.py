# Euclidean distance score is at it simplest a way to determine the similarity of people and how in common they are based off of things they have rankeduses include dating sites popular streming sites and personal ques.

def euclidean(p,q):
  sumSq=0.0
  
  # add up the squared differences
  for i in range(len(p)):
    sumSq+=(p[i]-q[i])**2
	
  # take the square root
  return (sumSq**0.5)
  
  
# real life example

from math import sqrt
 
# Returns a similarity score for person1 and person2
def sim_euclidean(prefs,person1,person2):
  # Get the list of shared_items
  si={}
  for item in prefs[person1]:
    if item in prefs[person2]:
	   si[item]=1
	   
   # if they have no raings in common, return 0
   if len(si)==0: return 0
   
   # Add up the squares of all the differences
   sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                       for item in si])
   
   return 1/(1+sqrt(sum_of_squares))
   
Then we can call this to execute a run to get our score.

>> import data
>> reload(data)
>> data.sim_euclidean(data.users,
... 'person1','person2')