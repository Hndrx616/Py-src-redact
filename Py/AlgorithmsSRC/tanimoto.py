def tanimoto(a,b):
  c=[v for v in a if v in b]
  return float(len(c))/(len(a)+len(b)-len(c))
  
  
# real example
def tanimoto(v1,v2):
  c1,c2,shr=0,0,0
  
  for i in range(len(v1)):
    if v1[i]!=0: c1+=1 # in v1
	if v2[i]!=0: c2+=1 # in v2
	if v1[i]!=0: and v2[i]!=0: shr+= # in both
	
  return 1.0-(float(shr)/(c1+c2-shr))

Then we call to execute.  

>> reload(analytics)
>> data=clusters.readfile('ratings.txt')
>> clust=clusters.hcluster(data,distance=clusters.tanimoto)