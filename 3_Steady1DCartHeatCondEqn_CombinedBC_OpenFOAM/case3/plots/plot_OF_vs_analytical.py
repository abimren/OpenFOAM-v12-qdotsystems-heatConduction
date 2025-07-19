import numpy as np
import matplotlib.pyplot as plt
# Set Runtime Configuration in family groups
plt.rc('figure',autolayout=True,figsize=(8,6))
#plt.rc('font',family='Arial',size=20)
plt.rc('font',size=18)
# *********************************************************
# Analytical - Left wall: conv + flux, Right wall: conv + flux
# Analytical case -> Negative qL is entering the domain  
q0=-1000 #W/m^2
hA=150  #W/m^2-K
TA=20 #C
qL=100   #W/m^2
hB=50  #W/m^2-K
TB=80  #C
k=3   #W/mK
L=10   #m
x=np.linspace(0,L,100)
T=TA+q0/hA+hA*hB*((TB-TA)-(q0/hA+qL/hB))/(hA*hB*L+k*(hA+hB))*(x+k/hA)
plt.plot(x,T,label='Analytical') 
# *********************************************************
file='../postProcessing/sample/3/line_centreProfile.xy'
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
