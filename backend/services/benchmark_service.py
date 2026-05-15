import time
import random
from core.models import Package, Container
from services.algorithm_service import AlgorithmService

def run_benchmark():
    service = AlgorithmService()
    sizes = [10, 100, 500, 1000] #cantidad de paquetes
    container = Container(max_weight=200) #contenedor grnde

    print("="*55)
    print("BENCHMARK DE ALGORITMOS: Dinamica vs Voraz")
    print("="*55)
    print(f"{'N (Paquetes)':<15} | {'Voraz O(n log n)':<18} | {'Dinámica O(n * W)':<18}")
    print("-" * 55)

    for n in sizes:
        packages = [
            Package(
                id=f"P{i}", 
                name=f"Item-{i}", 
                weight=random.randint(1, 50), 
                value=random.randint(10, 100)
            ) for i in range(n)
        ]

        start_greedy = time.perf_counter()
        service.optimize_greedy(packages, container)
        time_greedy = time.perf_counter() - start_greedy

        start_dp = time.perf_counter()
        service.optimize_dynamic_programing(packages, container)
        time_dp = time.perf_counter() - start_dp

        print(f"{n:<15} | {time_greedy:.6f}s{' ':>9} | {time_dp:.6f}s")
        
    print("="*55)

if __name__ == "__main__":
    run_benchmark()