"""This module is used to test a simple liner regression using scikit-learn"""

from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import datasets
from matplotlib import pyplot as plt


class LinearRegressionTest:
    def __init__(self):
        print "__init__ "
        # Load the diabetes dataset
        # diabetes = datasets.load_diabetes()
        # iris = datasets.load_iris()
        # print iris
        # Creating the regression model
        self.linear_regression_model = LinearRegression()

        """ TRAINING DATA """
        # data_set : [sq.ft. , room_no]
        self.training_X = np.array([[500, 1], [700, 2], [1000, 3], [1200, 1], [1500, 2], [1600, 4], [1700, 3], [1800, 5], [1900, 5], [2200, 6]])
        # target : [price]
        self.training_Y = np.array([10000, 12000, 14000, 17000, 19000, 25000, 30000, 35000, 45000, 60000])

        """ TEST DATA """
        self.test_X = np.array([[1200, 2], [1700, 4]])

        print "training_X_shape: ", self.training_X.shape
        print "training_Y_shape: ", self.training_Y.shape
        # print self.training_X[:, np.newaxis, 0]

    def train_data(self):
        # Fit the training data set
        self.linear_regression_model.fit(self.training_X, self.training_Y)

    def predict_data(self):
        print self.linear_regression_model.predict(self.test_X)

    def show_graph(self):
        plt.scatter(self.training_X[:, np.newaxis, 0], self.training_Y, color='green')
        plt.scatter(self.test_X[:, np.newaxis, 0], self.linear_regression_model.predict(self.test_X), color='blue')
        plt.plot(self.test_X[:, np.newaxis, 0], self.linear_regression_model.predict(self.test_X), color='red', linewidth = 1)
        plt.xlabel("Sq. Ft & Room No.")
        plt.ylabel("Price of flat")
        plt.title("Graphical representation of flat based on Size, Room No and Price")
        plt.show()


def main():
    lrt = LinearRegressionTest()
    lrt.train_data()
    # lrt.predict_data()
    lrt.show_graph()

main()


