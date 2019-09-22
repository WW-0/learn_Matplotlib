import matplotlib.pyplot as plt
import numpy as np

"""绘制正余弦"""
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # x是np的一个数组，包含从-Π到Π等间隔的256个数
C, S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)
plt.show()

"""绘图样式的配置"""
plt.figure(figsize=(8, 6), dpi=80)  # 创建一个8*6点（point）图，并设置分辨率为80
plt.subplot(1, 1, 1)  # 创建一个新的1*1的子图，接下来的图样绘制在其中的第一块（也是唯一一块）
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
# plt.plot(X, C, color='blue', linewidth=1.0, linestyle='-')  # 余弦，蓝色 连续 宽度为1(像素)的线条
# plt.plot(X, S, color='green', linewidth=1.0, linestyle='-')  # 正弦，绿色 连续 宽度为1(像素)的线条
# plt.xlim(-4.0, 4.0)  # 设置横轴上下限
# plt.xticks(np.linspace(-4, 4, 9, endpoint=True))  # 设置横轴记号
# plt.ylim(-1.0, 1.0)  # 设置纵轴上下限
# plt.yticks(np.linspace(-1, 1, 5, endpoint=True))  # 设置纵轴记号
plt.savefig('01基本绘图.jpg', dpi=72)

"""设置图片边界"""
xmin, xmax = X.min(), X.max()
ymin, ymax = S.min(), S.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
plt.xlim(xmin - dx, xmax + dx)
plt.ylim(ymin - dy, ymax + dy)

'''设置记号以及记号的标签'''
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],  # 设置记号
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])  # 设置记号的标签
plt.yticks([-1, 0, 1],  # 设置记号
           [r'$-1$', r'$0$', r'$+1$'])  # 设置记号的标签

'''移动spine脊柱到0点'''
ax = plt.gca()
ax.spines['right'].set_color('none')  # 脊柱功能
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

'''左上角添加图例'''
plt.plot(X, C, color='blue', linewidth=2.5, linestyle='-', label='cosine', zorder=-1)  # zorder控制绘图顺序
plt.plot(X, S, color='red', linewidth=2.5, linestyle='-', label='sine', zorder=-2)
plt.legend(loc='upper left')

'''特殊注释'''
# 希望在2π/3的位置给两条函数曲线加上一个注释。
# 首先在对应的函数图像位置上画一个点；
# 然后，向横轴引一条垂线，以虚线标记；
# 最后，写上标签
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle='--')
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')  # scatter 分布分散
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',  # annotate 注释
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.sin(t), ], 50, color='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 坐标轴上的记号标签被曲线挡住了，可以把它们放大，然后添加一个白色的半透明底色。这样可以保证标签和曲线同时可见
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))  # 此处如果失效请检查绘图顺序，即底层置顶之类属性
    # facecolor表面颜色 edgecolor边缘颜色 alpha透明度
plt.show()
