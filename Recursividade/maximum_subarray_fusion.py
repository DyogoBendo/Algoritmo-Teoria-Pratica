from maximum_subarray import maximum_subarray,maximum_subarray_fused
from maximum_subarray_bruto import maximum_subarray as max_brut
import random
import timeit

if __name__ == "__main__":
    a = [random.randint(-1000, 1000) for i in range(100)]
    
    print(a)

    print("Logaritimico: ", timeit.timeit(lambda: maximum_subarray(a, 0, len(a) -1), number=1))
    print("Quadratico:", timeit.timeit(lambda: max_brut(a), number=1))
    
    # Temos que para valores menores ou iguais a 50, o tempo da função quadrática é menor
    # Podemos implementar o caso base, para sempre que o valor for menor que 50, da função que usa o método divisão e conquista
    
    print("Fusao: ", timeit.timeit(lambda: maximum_subarray_fused(a, 0, len(a) -1), number=1))
    
    