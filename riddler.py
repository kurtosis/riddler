import numpy as np
results = np.zeros(10)
for i in range(10):
	if i==0:
		results[i]=0
	else:
		results[i] = i*(i+1)/(10*i+9)
		results[i] = results[i] + 1/(10*i+9)*results[:(i)].sum()
	print(f'{i} : {19*results.sum()/(i+1)}')
results.mean()
