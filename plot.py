""" Simple example of plotting using pyplot """
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    x = np.linspace(-2*np.pi,2*np.pi,1000)
    y = np.sin(x)
    plt.plot(x,y)
    plt.xlim(-2*np.pi,2*np.pi)
    plt.ylim(-1.5,1.5)
    plt.legend(["$ y=sin(x) $"])
    plt.show()
