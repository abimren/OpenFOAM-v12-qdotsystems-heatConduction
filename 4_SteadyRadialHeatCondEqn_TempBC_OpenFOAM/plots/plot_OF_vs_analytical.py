import numpy as np
import matplotlib.pyplot as plt
# Set Runtime Configuration in family groups
plt.rc('figure',autolayout=True,figsize=(8,6))
#plt.rc('font',family='Arial',size=20)
plt.rc('font',size=18)
# *********************************************************
# Analytical - Radial Left Right wall: Fixed T
r1=0.03  #m
T1=100 #C
r2=0.07  #m
T2=20  #C
k=4   #W/mK
r=np.linspace(r1,r2,100)
T=(T1-T2)/np.log(r1/r2)*np.log(r/r1)+T1
plt.plot(r,T,label='Analytical') 
# *********************************************************
file='../postProcessing/sample/5/line1.xy'
#file='../postProcessing/sample/3/line_centreProfile_T.xy'
data=np.loadtxt(file)
print(file,data.shape,data[0])
rad=np.sqrt(data[:,0]**2+data[:,1]**2)
plt.plot(rad,data[:,3],'^--',lw=2,label='OF',ms=10,mfc="none",markevery=1)
plt.ylabel('Temperature (C)')
plt.xlabel('Length (m)')
plt.legend()
#plt.xlim((0,10))
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
