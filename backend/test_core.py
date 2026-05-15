from core.models import Container
from core.data_repository import PackageRepository
from services.algorithm_service import AlgorithmService

def run_tests():
    repo = PackageRepository()
    service = AlgorithmService()

    packages = repo.get_all_packages()
    container = Container(max_weight=50)

    print("Iniciando simulacion: IntelliCargo System")
    print(f"Capacidad del contenedor: {container.max_weight}kg\n")

    print("--- Estrategia: programacion dinamica ---")
    dp_result = service.optimize_dynamic_programing(packages, container) 
    print(f"Valor max: ${dp_result['max_value']}") 
    print(f"Peso utilizado: {dp_result['total_weight']}kg")
    print(f"Paquetes: {[p.name for p in dp_result['selected_items']]}\n")

    print("--- estrategia: algoritmo voraz ---")
    greedy_result = service.optimize_greedy(packages, container)
    print(f"Valor max: ${greedy_result['max_value']}")
    print(f"Peso utilizado: {greedy_result['total_weight']}kg") 
    print(f"Paquetes: {[p.name for p in greedy_result['selected_items']]}\n")

if __name__ == "__main__":
    run_tests()