import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library (adjust path to the correct location)
lib = ctypes.CDLL('./output.so')  # Replace with './func.dll' on Windows

# Define argument and return types for the C functions
lib.solution.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.solution.restype = None

# Set the initial values and parameters
x = ctypes.c_float(0.0)  # Initial value of x
area = ctypes.c_float(0.0)  # Initial value of the area
n = int(2 * np.pi / 0.001)  # Number of iterations based on step size h

# Create arrays to store the results for plotting
x_vals = []
cos_vals = []
intersections_x = []  # List to store x-coordinates of intersections
intersections_y = []  # List to store y-coordinates (all zeros for intersections)

# Run the solution function and store results for plotting
h = 0.0001  # Step size
for i in range(n + 1):
    # Append current values to the lists
    x_vals.append(x.value)
    cos_val = np.cos(x.value)
    cos_vals.append(cos_val)
    
    # Check for intersections (y = 0)
    if i > 0 and cos_vals[i - 1] * cos_val < 0:  # Sign change indicates intersection
        intersections_x.append(x.value)
        intersections_y.append(0)
    
    # Call the C solution function
    lib.solution(ctypes.byref(x), ctypes.byref(area), 1)

# Plot the graph and fill the area under the curve
plt.figure(figsize=(12, 8))
plt.plot(x_vals, cos_vals, label="cos(x)", color='b', linewidth=2)
plt.fill_between(x_vals, cos_vals, color='blue', alpha=0.3, label="Area under cos(x)")
plt.xlim([0, 2 * np.pi])
plt.ylim([-1.1, 1.1])
plt.xlabel("x-axis")
plt.ylabel("cos(x)")
plt.axhline(0, color='black', linewidth=1)  # x-axis

# Plot and label the points of intersection
for x_int in intersections_x:
    plt.scatter(x_int, 0, color='red', zorder=5)  # Plot the point
    plt.text(x_int, 0.1, f"({x_int:.2f}, 0)", color='blue', fontsize=10, ha='center')  # Label the point

# Add legends, grid
plt.legend()
plt.grid(True)
plt.show()

