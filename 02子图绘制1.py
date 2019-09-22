import matplotlib.pylab as plt

plt.subplot(2, 1, 1)  # 创建次图 ,参数1x 参数2y方向分别有几个图，参数3图编号(从1开始)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,1,1)', ha='center', va='center', size=24, alpha=.5)
# x,y,title,horizontalalignment水平对齐方式,verticalalignment,fontsize文字大小

plt.subplot(2, 1, 2)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,1,2)', ha='center', va='center', size=24, alpha=.5)

plt.show()

plt.subplot(1, 2, 1)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'subplot(1,2,1)', ha='center', va='center', size=24, alpha=.5)

plt.subplot(1, 2, 2)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'subplot(1,2,2)', ha='center', va='center', size=24, alpha=.5)

plt.show()

plt.subplot(2, 2, 1)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,2,1)', ha='center', va='center', size=24, alpha=.5)

plt.subplot(2, 2, 2)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center', size=24, alpha=.5)

plt.subplot(2, 2, 3)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,2,3)', ha='center', va='center', size=24, alpha=.5)

plt.subplot(2, 2, 4)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,2,4)', ha='center', va='center', size=24, alpha=.5)

plt.show()
