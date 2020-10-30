import numpy as np

class LinearRegression:

    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr                # learning rate for gradient search
        self.n_iters = n_iters      # iterations for fitting line of regression
                                    # y = mx + c
        self.m = None               # slope of the line
        self.c = None               # intersection with y axis


    # looking for optimal m and c coefficients
    def fit(self, X_train, y_train):
        # initialization
        n_samples, n_features = X_train.shape     # 80 rows x 1 column
        self.m = np.zeros(n_features)             # [0.]
        self.c = 0                                # starting with zero

        # gradient search - fitting regression line to actual data
        for _ in range(self.n_iters):

            #  [...          *    [0.]    =     [0. 0 . 0. ...]
            #   [0.123]
            #   [0.456]
            #   [0.789]
            #       ...]

            # (80,1)        *   (1,)       =  (80,)

            y_predicted = np.dot(X_train, self.m) + self.c

            #  first iteration - one dimension array
            #  y_predicted = [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
            #  0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
            #  0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. ]

            dm = (1/n_samples) * np.dot(X_train.T, (y_predicted - y_train))
            # X_train.T transposing:
            #  [...             =>    [[... 0.123 0.123 0.123 ... ]]
                # [0.123]
                # [0.123]
                # [0.123]
                # ...]

            dc = (1/n_samples) * np.sum(y_predicted - y_train)

            # updating m and c coefficients with each iteration
            self.m = self.m - self.lr * dm
            self.c = self.c - self.lr * dc

    def predict(self, X):
        # using optimal m and c coefficients
        y_predicted = np.dot(X, self.m) + self.c
        return y_predicted
