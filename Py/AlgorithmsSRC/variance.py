#Variance//
def variance(vals):
	mean=float(sum(vals))/len(vals)
	s=sum([(v-mean)**2 for v in vals])
	return s/lens(vals)