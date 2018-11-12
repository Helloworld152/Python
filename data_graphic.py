"""
运用matplotlib进行数据可视化
"""

import matplotlib.pyplot as plt
"""输入数据"""
input_values = list(range(1,6))
squares = [1,4,9,16,25]
x_values = list(range(1, 1001))
y_values = [x**3 for x in x_values]

plt.plot(input_values, squares, linewidth = 5)
plt.scatter(x_values, y_values, c =  'red', edgecolors='none', s = 40)
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolors='none', s = 40)

"""标题"""
plt.title("Square Numbers", fontsize = 24)

"""横坐标"""
plt.xlabel("Value", fontsize = 14)

"""纵坐标"""
plt.ylabel("Square of Value", fontsize = 14)

"""刻度标记的大小"""
plt.tick_params(axis='both', labelsize = 14)

"""设置每个坐标轴的取值范围"""
plt.axis([0, 1100, 0, 1100000000])


"""保存图像，在show之前调用"""
plt.savefig('square_plot1.png', bbox_inches = 'tight')

plt.show()
