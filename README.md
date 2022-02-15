# 1D Advection Wave Code for Testing
1D Advection Problem represents wave travelling. This code output a height data in 1D space domain. Simply put, the code simulates a sine wave travelling rightward with a periodic boundary conditions (The wave loop itself when touching the boundary).
Since all wave can be formed by a series of sine and cosine wave, the 1D advection problem can be used as a first test our model architecure.
The output U matrix has the structure: the row represents different time step; the columns represents different point in space.

# Output Training Data
Assume we use N=3 numbers of frames as the training input. At each time step i, the code collect the output U(or height) from time step (i,i+1,i+2), reshape it into a row vector, and store it as the i-th X-train data. Then the code stores the output U(or height) at time step (i+3) as the i-th Y-train data.

# Training Objective
Given the i-th X-train data, construct a model that can generate a Y-predict data that is similar to the i-th Y-train data.

# Next Test
1D Diffusion Problem (Wave spread out)
