import numpy as np
import math
import matplotlib.pyplot as plt

def u(x,t):
    k = 1;
    w = 1;
    return math.sin(k*x-w*t);

def main():
    tres = 100;
    xres = 1000;
    t = np.linspace(0,9,tres);
    x = np.linspace(0,2*np.pi,xres);
    U = np.zeros((tres,xres));

    for i in range(tres):
        t0 = t[i];
        for j in range(xres):
            x0 = x[j];
            U[i,j] = u(x0,t0);

    # Display Data
    np.set_printoptions(precision=2)
    np.set_printoptions(suppress=True)
    print("Output U Data:");
    print(U);
    print("Shape of U:",U.shape);

    # Extract (X,Y) Training Data, Nsample = 3
    Nsample = 3;
    i = 0;
    X_train = np.zeros((tres,xres*Nsample));
    Y_train = np.zeros((tres,xres));
    for i in range(0,tres-Nsample):
        X_train[i,:] = np.reshape(U[i:i+Nsample,:],-1); # Combine first 3 time frame U data into a row vector
        Y_train[i,:] = U[i+Nsample,:];

    print("\n");
    print("X_train Data");
    print(X_train);
    print("X_train Shape: ",X_train.shape);
    print("\n");
    print("Y_train Data");
    print(Y_train);
    print("Y_train Shape: ",Y_train.shape);

    # Visualize Wave
    # Blue lines are the input X vector
    # Red  line  is  the output Y vector
    plt.figure;
    plt.plot(x,U[0,:],color='blue');
    plt.plot(x,U[1,:],color='blue');
    plt.plot(x,U[2,:],color='blue');
    plt.plot(x,U[3,:],color='red');
    plt.plot(x,U[50,:],color='blue');
    plt.plot(x,U[51,:],color='blue');
    plt.plot(x,U[52,:],color='blue');
    plt.plot(x,U[53,:],color='red');
    plt.show();



if __name__ == "__main__":
    main()
