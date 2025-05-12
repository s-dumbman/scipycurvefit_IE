import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def true_func(x):
    return 2 * x**2 + 3 * x + 5

x_data = np.linspace(-5, 5, 50)
y_data = true_func(x_data) + np.random.normal(0, 5, size=x_data.shape)

def model_func(x, a, b, c):
    return a * x**2 + b * x + c

params, covariance = curve_fit(model_func, x_data, y_data)
a_fit, b_fit, c_fit = params

print(f"a = {a_fit:.2f}, b = {b_fit:.2f}, c = {c_fit:.2f}")

plt.scatter(x_data, y_data, label='data', color='blue')
plt.plot(x_data, model_func(x_data, *params), color='red', label='fitted curve')
plt.plot(x_data, true_func(x_data), '--', color='green', label='true curve')
plt.title("curve_fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
