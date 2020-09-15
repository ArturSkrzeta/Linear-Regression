import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

def mim_squared_error(y_actual, y_predicted):
    mse = np.mean((y_actual - y_predicted)**2)
    print('MSE for the model: ' + str(round(mse,2)))

def plot_lr(y_predicted):
    cmap = plt.get_cmap('viridis')
    plt.figure(figsize=(8,6))
    plt.scatter(X_test, y_test, color=cmap(0.9), s=10)
    plt.plot(X_test, y_predicted)
    plt.show()

def plot_sample(new_sample, y_predicted):
    cmap = plt.get_cmap('viridis')
    plt.figure(figsize=(8,6))
    plt.scatter(new_sample, y_predicted, color=cmap(0.5), s=20)
    plt.show()

class LinearRegression:

    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr                # learning rate for gradient search
        self.n_iters = n_iters      # iterations for fitting line of regression
                                    # y = mx + c
        self.m = None               # slope of the line
        self.c = None               # intersection with y axis

    def fit(self, X_train, y_train):
        # initialization
        n_samples, n_features = X_train.shape     # 80 rows x 1 column
        self.m = np.zeros(n_features)             # [0.]
        self.c = 0                                # starting with zero

        # gradient search - fitting regression line to actual data
        for _ in range(self.n_iters):

            #  first iteration
            #  y_predicted = [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
            #  0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
            #  0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. ]


            #  [...          *    [0.]    =     [0. 0 . 0. ...]
                # [0.123]
                # [0.456]
                # [0.789]
                # ...]


            #                      (80,1), (1,)
            y_predicted = np.dot(X_train, self.m) + self.c

            # X_train.T transposing:
            #  [...             =>    [[... 123 123 123 ... ]]
                # [123]
                # [123]
                # [123]
                # ...]

            dm = (1/n_samples) * np.dot(X_train.T, (y_predicted - y_train))     # change of m coefficient
            dc = (1/n_samples) * np.sum(y_predicted - y_train)                  # change of c coefficient
                                                                                # with each iteration
            # updating m and c coefficients
            self.m = self.m - self.lr * dm
            self.c = self.c - self.lr * dc

    def predict(self, X):
        # using optimal m and c coefficiens
        y_predicted = np.dot(X, self.m) + self.c
        return y_predicted


def main():

    global X, y
    X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_predicted = regressor.predict(X_test)

    # the lower mse the better line fit
    mim_squared_error(y_test, y_predicted)
    plot_lr(regressor.predict(X_test))

    new_sample = np.array([[0.90],[1.20],[-0.50],[-1.13],[0.80],[-1.5],[0.99],[1.55]])
    y_predicted_from_new_sample = regressor.predict(new_sample)
    plot_sample(new_sample, y_predicted_from_new_sample)


if __name__ == "__main__":
    main()
