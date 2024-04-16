import numpy as np
import random
import math

def polinomio(x):
    # x**4 + 3*x**3 + 2*x**2 - 1
    return x**2 - 3*x -8

def simulated_annealing(func, x0, T, alpha, stopping_T, max_iter):
    # Inicialización
    x_curr = x0  # Solución actual
    x_best = x0  # Mejor solución
    f_curr = func(x_curr)
    f_best = f_curr
    
    iter = 0
    while T > stopping_T and iter < max_iter:
        x_next = x_curr + random.uniform(-10, 10)
        
        f_next = func(x_next)
        
        delta_E = f_next - f_curr
        
        # Decide si se acepta la nueva solución
        if delta_E < 0 or random.uniform(0, 1) < math.exp(-delta_E / T):
            x_curr = x_next
            f_curr = f_next
            
            # Actualiza la mejor solución encontrada
            if f_next < f_best:
                x_best = x_next
                f_best = f_next
        
        # Enfriamiento
        T = T * alpha
        iter += 1
    
    return x_best, f_best

# Parámetros del algoritmo
x0 = random.uniform(-10, 10)  # Punto inicial
T = 1.0  # Temperatura inicial
alpha = 0.60  # Tasa de enfriamiento
stopping_T = 1e-8  # Temperatura final
max_iter = 10000  # Número máximo de iteraciones

# Ejecuta el algoritmo
x_min, f_min = simulated_annealing(polinomio, x0, T, alpha, stopping_T, max_iter)

print(f"El mínimo aproximado es en x = {x_min} con un valor de {f_min}")

