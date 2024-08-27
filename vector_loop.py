#with numpy vectoization is faster
import numpy as np
import time
start=time.time()
a=np.sum(np.arange(1,500000))
print(a)
end=time.time()
print(end-start)
#with for loop is bit slow
start=time.time()
t=0
for i in range(1,500000):
    t+=i
print(t)    
end=time.time()
print(end-start)