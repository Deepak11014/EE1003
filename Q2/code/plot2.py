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
modulus_area = 0.0  # Accumulate absolute area
n = int(2 * np.pi / 0.001)  # Number of iterations based on step size h

# Create arrays to store the results for plotting
x_vals = []
sin_vals = []

# Run the solution function and store results for plotting
h = 0.001  # Step size
for i in range(n + 1):
    # Append current values to the lists
    x_vals.append(x.value)
    sin_vals.append(np.sin(x.value))
    
    # Accumulate the modulus value of sin(x)
    modulus_area += abs(np.sin(x.value)) * h
    
    # Call the C solution function
    lib.solution(ctypes.byref(x), ctypes.byref(area), 1)

# Print the modulus area
print(f"Modulus area under sin(x) from 0 to 2π: {modulus_area:.6f}")

# Plot the graph and fill the area under the curve
plt.figure(figsize=(10, 6))
plt.plot(x_vals, sin_vals, label="sin(x)", color='b', linewidth=2)
plt.fill_between(x_vals, sin_vals, color='blue', alpha=0.3, label="Modulus Area under sin(x)")
plt.xlim([0, 2 * np.pi])
plt.ylim([-1.1, 1.1])
plt.xlabel("x-axis")
plt.ylabel("sin(x)")
plt.title("Graph of sin(x) with Highlighted Modulus Area Under the Curve")
plt.axhline(0, color='black', linewidth=1)  # x-axis
plt.legend()
plt.grid(True)
plt.show()

