# Kmeans Algorithm realization
这是我用Python实现了Kmeans算法，测试用例是34省份人均支出数据, 如果需要测试不同数据，初始构造函数从文件读取数据部分需要改写，（将数据保存为无空格np.array 类型即可)。main 函数根据不同测试用例调整即可。jcosPlot（）方法用来观察cost fuction value “J”随K值的变化情况，根据Elbow method, 可以得出最佳的分类数目。
