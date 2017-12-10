import numpy as np
import numpy.random as random
from numpy import linalg as LA
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

class KMeans:
    def __init__(self,filePath,data=None,xRow = 0,xCol = 0):
        self.filePath = filePath
        fr = open(filePath,'r+')
        lines = fr.readlines()
        retData = []
        retCityName = []
        for line in lines:
            items = line.strip().split(",")
            retCityName.append(items[0])
            retData.append([float(items[i])  for i in range(1,len(items))])
        self.dataName = retCityName
        self.data = np.array(retData)
        self.xRow, self.xCol = [i for i in self.data.shape]

    def IntialCentroids(self,K):
        randomX = random.permutation(self.data)
        centroids = randomX[0:K, :]
        idx = self.findClosetCentroids(centroids)
        jSumMin = self.cosFunc(idx,centroids)
        #Random intial and choose the best begin Centroids with lowest cost function value J
        for i in range(100):
            randomX = random.permutation(self.data)
            tempCentroids = randomX[0:K, :]
            idx = self.findClosetCentroids(tempCentroids)
            newCentroids = self.computeCentroids(idx,K)
            jSum = self.cosFunc(idx,newCentroids)
            if jSum < jSumMin:
                centroids = newCentroids
                jSumMin = jSum
            else:
                continue
        return centroids

    def cosFunc(self,idx,centroids):
        jSum = 0
        for i in range(self.xRow):
            jSum = LA.norm(self.data[i,:] - centroids[int(idx[i]-1), :]) + jSum
        jSum = jSum/(self.xRow)
        return jSum

    def findClosetCentroids(self, centroids):
        kSize, kFeatures = [i for i in centroids.shape]
        idx = np.zeros((self.xRow, 1))
        for i in range(self.xRow):
            idx[i] = 1
            norm_min = LA.norm(self.data[i, :] - centroids[1, :])
            for j in range(kSize):
                if LA.norm(self.data[i, :] - centroids[j, :]) < norm_min:
                    norm_min = LA.norm(self.data[i, :] - centroids[j, :])
                    idx[i] = j
        return idx

    def computeCentroids(self,idx,K):
        centroids_matrix = np.zeros((K,self.xRow))
        centroids = np.zeros((K,self.xCol))
        CK = np.zeros((K,1))
        for i in range (self.xRow):
            centroids_matrix[int(idx[i]),i] = 1
            CK[int(idx[i])] = CK[int(idx[i])] + 1
        for i in range(K):
            centroids_Temp = np.dot(centroids_matrix,self.data)
            centroids[i,:] = centroids_Temp[i,:]/CK[i,:]
        return centroids

    def jCostPlot(self,kNum):
        x_data_plot = []
        y_data_plot = []
        for i in range(kNum):
            x_data_plot.append(i + 2)
            centroids = U.IntialCentroids(i + 2)
            for j in range(300):
                idx = U.findClosetCentroids(centroids)
                centroids = U.computeCentroids(idx, i + 2)
                jCos = U.cosFunc(idx, centroids)
            y_data_plot.append(jCos)
        x_data = np.array(x_data_plot)
        y_data = np.array(y_data_plot)
        xNew = np.linspace(x_data.min(), x_data.max(), 300)
        ySmooth = spline(x_data, y_data, xNew)
        plt.plot(xNew, ySmooth)
        plt.show()
        return None

if __name__=='__main__':
    U = KMeans('city.txt')
    centroids = U.IntialCentroids(4)
    for i in range(300):
        idx = U.findClosetCentroids(centroids)
        centroids = U.computeCentroids(idx, 4)
    labeled_City = [[], [], [], []]
    for i in range(len(U.dataName)):
        labeled_City[int(idx[i])].append([U.dataName[i]])
    for i in range(4):
        print(labeled_City[i])
    '''If want to see the cost function value change accompanied with K value, use the
        U.jCostPlot(K_Num), K_Num is the classification numbers , u can choose 10 to see what
        will plot out. According to eblow methond, u can find the best classification numbers.

