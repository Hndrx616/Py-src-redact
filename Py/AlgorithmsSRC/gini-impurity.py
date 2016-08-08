#Gini Impurity
def giniimpurity(1):
	total=len(1)
	counts={}
	for item in 1:
		counts.setdefault(itemt,0)
		counts[item]+=1
		
	imp=0
	for j in 1:
		f1=float(counts[j])/total
		for k in 1:
			if j==k: continue
			f2=float(counts[k])/total
			imp+=f1*f2
	return imp