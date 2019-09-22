import matplotlib.pylab as plt

plt.axes([0.1, 0.1, 0.8, 0.8])  # 参数1参数2图像xy坐标，参数3参数4图像宽高
plt.xticks([])
plt.yticks([])
plt.text(0.6, 0.6, 'axes([0.1,0.1,.8,.8])', ha='center', va='center', size=20, alpha=.5)

plt.axes([0.2, 0.2, 0.3, 0.3])
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'axes([0.2,0.2,.3,.3])', ha='center', va='center', size=16, alpha=.5)

plt.show()

plt.axes([0.1, 0.1, .5, .5])
plt.xticks([])
plt.yticks([])
plt.text(0.1, 0.1, 'axes([0.1,0.1,.5,.5])', ha='left', va='center', size=16, alpha=.5)

plt.axes([0.2, 0.2, .5, .5])
plt.xticks([])
plt.yticks([])
plt.text(0.1, 0.1, 'axes([0.2,0.2,.5,.5])', ha='left', va='center', size=16, alpha=.5)

plt.axes([0.3, 0.3, .5, .5])
plt.xticks([])
plt.yticks([])
plt.text(0.1, 0.1, 'axes([0.3,0.3,.5,.5])', ha='left', va='center', size=16, alpha=.5)

plt.axes([0.4, 0.4, .5, .5])
plt.xticks([])
plt.yticks([])
plt.text(0.1, 0.1, 'axes([0.4,0.4,.5,.5])', ha='left', va='center', size=16, alpha=.5)

plt.show()
