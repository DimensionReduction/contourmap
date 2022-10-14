
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

data=pd.read_excel('数据.xls',sheet_name='附件1',usecols=['x(m)','y(m)','海拔(m)'],header=2)
x=data.iloc[:,0]
y=data.iloc[:,1]
z=data.iloc[:,2]
xi=np.linspace(min(x),max(x))
yi=np.linspace(min(y),max(y))
xi,yi=np.meshgrid(xi,yi)
zi=griddata(data.iloc[:,0:2],z,(xi,yi),method='cubic')
levels=np.linspace(np.min(z),np.max(z),30)

fig,ax=plt.subplots(figsize=(8,6))
cs=ax.contour(xi,yi,zi,levels=levels)
ax.clabel(cs,inline=True,fontsize=6)
ax.set_title('等高线图')
plt.show()
