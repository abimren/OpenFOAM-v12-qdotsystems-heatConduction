import numpy as np
import matplotlib.pyplot as plt
# Set Runtime Configuration in family groups
plt.rc('figure',autolayout=True,figsize=(8,6))
#plt.rc('font',family='Arial',size=20)
plt.rc('font',size=18)
# *********************************************************
# Analytical - both left and right fixed T
T1=100
T2=20
L=10
x=np.linspace(0,L,100)
T=(T2-T1)/L*x + T1
plt.plot(x,T,label='Analytical') 
# *********************************************************
file='../postProcessing/sample/10/line_centreProfile.xy'
data=np.loadtxt(file)
print(file,data.shape,data[0])
plt.plot(data[:,0],data[:,1],'^--',lw=2,label='OF',ms=10,mfc="none",markevery=10)
plt.ylabel('Temperature (C)')
plt.xlabel('Length (m)')
plt.legend()
plt.xlim((0,10))
#plt.ylim((0,300))
#plt.ylim(bottom=-1000) 
plt.grid(ls='--')
plt.savefig(f"temp.png")
plt.show()
# line  '-',':','--','-.'
# color r,g,b,c,m,y,k,w
# marker o,*,v,^,<,>,s,D,  d,x,X,+,P,p,h,1,2,3,4,|
# marker color e.g., mfc="blue", mfc="none"
# format: 'marker line color' e.g., 'D-k' 
#plt.plot(results[:,0],results[:,1],'s-.',label='DVODE',ms=10,mfc="none",markevery=5)
