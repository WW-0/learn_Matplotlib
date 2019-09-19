import matplotlib.pyplot as plt
import numpy as np

"""绘制正余弦"""
X=np.linspace(-np.pi,np.pi,256,endpoint=True) #x是np的一个数组，包含从-Π到Π等间隔的256个数
C,S=np.cos(X),np.sin(X)
plt.plot(X,C)
plt.plot(X,S)
plt.show()

"""绘图样式的配置"""
plt.figure(figsize=(8,6),dpi=80)#创建一个8*6点（po,int）图，并设置分辨率为80
plt.subplot(1,1,1)#创建一个新的1*1的子图，接下来的图样绘制在其中的第一块（也是唯一一块）
X=np.linspace(-np.pi,np.pi,259,endpoint=True)
C,S=np.cos(X),np.sin(X)
plt.plot(X,C,color='blue',linewidth=1.0,linestyle='-')#余弦，蓝色 连续 宽度为1(像素)的线条
plt.plot(X,S,color='green',linewidth=1.0,linestyle='-')#正弦，绿色 连续 宽度为1(像素)的线条
plt.xlim(-4.0,4.0)#设置横轴上下限
plt.xticks(np.linspace(-4,4,9,endpoint=True))#设置横轴记号
plt.ylim(-1.0,1.0)#设置纵轴上下限
plt.yticks(np.linspace(-1,1,5,endpoint=True))#设置纵轴记号
plt.savefig('01基本绘图.jpg',dpi=72)
plt.show()