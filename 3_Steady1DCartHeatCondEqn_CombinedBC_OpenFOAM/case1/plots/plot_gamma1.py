import numpy as np
import matplotlib.pyplot as plt
# Set Runtime Configuration in family groups
plt.rc('figure',autolayout=True,figsize=(8,6))
#plt.rc('font',family='Arial',size=20)
plt.rc('font',size=18)
# *********************************************************
L=0.2
x=np.linspace(0,L,100)
def calc(lambd,gamma):
  if gamma == 1:
    YoverYin=(1-1/lambd)**(x/L)
    joverjbar= -lambd*np.log((1-1/lambd))*(1-1/lambd)**(x/L)
  else :
    term=1-(1-1/lambd)**(1-gamma)
    YoverYin=(1-term*(x/L))**(1/(1-gamma))
    joverjbar= lambd*term/(1-gamma)*(1-term*(x/L))**(gamma/(1-gamma))
  return YoverYin,joverjbar 
plt.figure(1)
gamma=1
lambd=2
YoverYin_2,joverjbar_2=calc(lambd,gamma)
plt.plot(x/L,YoverYin_2,label='Analytical $\lambda = 2$')
lambd=1.1
YoverYin_11,joverjbar_11=calc(lambd,gamma)
plt.plot(x/L,YoverYin_11,label='Analytical $\lambda = 1.1$')
lambd=1.01
YoverYin_101,joverjbar_101=calc(lambd,gamma)
plt.plot(x/L,YoverYin_101,label='Analytical $\lambda = 1.01$')
plt.xlabel('x/L')
plt.ylabel('$Y/Y_{i}$')
plt.xlim((0,1))
plt.ylim((0,1)) 
#plt.xlim(right=0.2)
plt.grid(ls='--')
plt.legend(fontsize=12)
#plt.savefig(f"dP.png")

plt.figure(2)
plt.plot(x/L,joverjbar_2,label='Analytical $\lambda = 2$')
plt.plot(x/L,joverjbar_11,label='Analytical $\lambda = 1.1$')
plt.plot(x/L,joverjbar_101,label='Analytical $\lambda = 1.01$')
plt.xlabel('x/L')
plt.ylabel(r'$j/ \bar{j}$')
plt.xlim((0,1))
plt.ylim(bottom=0) 
plt.grid(ls='--')
plt.legend(fontsize=12)
plt.show()
"""
file='../postProcessing/pressureDrop/0/fieldValueDelta.dat'
data=np.loadtxt(file)
print(file,data.shape,data[0])
plt.plot(data[:,0],rho*data[:,1],'navy',lw=2,label='$dP (Pa)$')
"""