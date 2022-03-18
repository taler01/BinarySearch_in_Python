import numpy
import scipy
import matplotlib
import requests
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def sklearn_test():
    iris = load_iris()
    print("数据集是： \n", iris)
    print("数据集描述： \n", iris["DESCR"])

    #数据集划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                        test_size=0.2, random_state=22)
    print("")
    return None


if __name__ == '__main__':
    sklearn_test()