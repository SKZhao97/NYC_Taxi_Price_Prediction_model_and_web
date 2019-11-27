#-*- coding:utf-8 -*-  

import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.cluster import KMeans
from csv import reader
import csv
from scipy.spatial.distance import cdist  

filename = "test.csv"
raw_data = open(filename, 'rt', encoding='UTF-8')
readers = reader(raw_data, delimiter=',')
string_data = np.array(list(readers)).transpose()
# print(data[1])
data = string_data.astype(np.float)
x = data[0]
y = data[1]
xm = np.max(data[0])
ym = np.max(data[1])
data = data.transpose()
# 输入数据，类型为np.array
# K-Means参数的最优解也是以成本函数最小化为目标  
# 成本函数是各个类畸变程度（distortions）之和。每个类的畸变程度等于该类重心与其内部成员位置距离的平方和
'''
aa=[]
K = range(1, 10) 
for k in range(1, 10):
    kmeans=KMeans(n_clusters=k) 
    kmeans.fit(data) 
    aa.append(sum(np.min(cdist(data, kmeans.cluster_centers_, 'euclidean'), axis=1))/data.shape[0])
plt.figure() 
plt.plot(np.array(K), aa, 'bx-') 
plt.show()
'''
# 绘制散点图及聚类结果中心点
# plt.figure()
# plt.axis([0, xm+20, 0, ym+20])
# plt.grid(True)
# plt.plot(x, y, 'k.')
kmeans = KMeans(n_clusters=6)
# 进行聚类
kmeans.fit(data)
label = kmeans.labels_
centers = kmeans.cluster_centers_
# print(label)
# print(centers)
# plt.plot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 'r.')
# plt.show()
# 保存到新的csv
path = "result.csv"
f = open(path, 'w', newline='')
csv_write = csv.writer(f)
for i in range(data.shape[0]):
    data_row = [data[i][0], data[i][1], label[i]]
    csv_write.writerow(data_row)


