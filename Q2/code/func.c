#include <stdio.h>
#include <math.h>
#include <stdlib.h> // For fabs

double trapezoidal_cos(double x1, double x2, int n) {
    double h = fabs(x2 - x1) / n;
    double A = 0;
    double n = 1000000;

    // Correctly handle the case where x1 > x2
    double start = fmin(x1, x2);
    double end = fmax(x1, x2);
    
    //Optimization: precalculate cos for endpoints
    double f_start = cos(start);
    double f_end = cos(end);
    
    A = (f_start + f_end) / 2.0; //first and last terms are divided by 2
    
    for (int i = 1; i < n; i++) {
        double x = start + i * h;
        A += cos(x);
    }
    A *= h;
    return fabs(A); // Return absolute value for area
}
