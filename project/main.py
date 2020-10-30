import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from lr import LinearRegression

def mim_squared_error(y_actual, y_predicted):
    mse = np.mean((y_actual - y_predicted)**2)
    print('MSE for the model: ' + str(round(mse,2)))

def plot_chart(y_predicted):

    cmap = plt.get_cmap('viridis')
    plt.figure(figsize=(8,6))
    plt.xlabel('sample feature')
    plt.ylabel('value')
    plt.scatter(X_test, y_test, color=cmap(0.9), s=50)
    plt.plot(X_test, y_predicted, linewidth=3)
    plt.show()

def main():

    # generating data
    global X, y
    X, y = datasets.make_regression(n_samples=300, n_features=1, noise=10, random_state=3)
    X = np.array([abs(x) for x in X])
    y = np.array([abs(_y) for _y in y])

    print(X)
    print(y)

    # splitting data into training and testing sets
    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    # training model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    #testing model
    y_predicted = regressor.predict(X_test)
    # the lower mse the better line fit
    mim_squared_error(y_test, y_predicted)
    plot_chart(y_predicted)

    # predicitng values for new sample features
    new_sample = np.array([[0.90],[1.20],[0.80],[0.99],[1.55]])
    y_predicted_from_new_sample = regressor.predict(new_sample)
    print(y_predicted_from_new_sample)

if __name__ == "__main__":
    main()
