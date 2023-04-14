# NPM: 2006537324
# f(x) = 2**0 + 0**6 + 5**3 + 7**3 + 2**4
# f(x) = 1 + 12*x**3 + 2*x**4
import numpy as np
import matplotlib.pyplot as plt

# Define function to integrate
def f(x):
    return 1 + 12*x**3 + 2*x**4

# Implementing trapezoidal method
def trapezoidal(a,b,n):
    # calculating step size
    h = (b - a) / n
    
    # Finding sum 
    integration = f(a) + f(b)
    
    for i in range(1,n):
        k = a + i*h
        integration = integration + 2 * f(k)
    
    # Finding final integration value
    integration = integration * h/2
    
    return integration
    
# Input section
a = 1
b = 5
n = 100

# Call trapezoidal() method and get result
result = trapezoidal(a, b, n)

#exact value = 3125.6
err_result = abs(((3125.6 - result)/3125.6)*100)
print("Integration result by Trapezoidal method is: %0.6f" % (result))
print("The error of trapezoidal integration is: %0.4f" % (err_result), '%')

# x and y values for the trapezoid rule
x = np.linspace(a,b,n+1)
y = [f(i) for i in x]  # this is a change

# X and Y values for plotting y=f(x)
X = np.linspace(a,b,5)
Y = [f(j) for j in X]  #this is a change
plt.plot(X,Y)

for i in range(n):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

plt.title('Trapezoid Rule, N = {}'.format(n))
plt.show()