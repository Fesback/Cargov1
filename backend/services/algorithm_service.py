from core.models import Package, Container

class AlgorithmService:
    def optimize_dynamic_programing(self, packages: list[Package], container: Container) -> dict:
        """
        Resolveremos el problema de mochila 0/1 usando programacion dinamica, en otros terminos
        0(n * W) donde n = len (packages) y w = container.max_weight
        """

        n = len(packages)
        w_max = container.max_weight

        dp = [[0 for _ in range(w_max + 1)] for _ in range(n + 1)]

        for i in range (1, n + 1):
            current_pack = packages[i-1]
            for w in range(1, w_max + 1):
                if current_pack.weight <= w:
                    dp[i] [w] = max (
                        current_pack.value + dp[i - 1][w - current_pack.weight],
                        dp [i - 1][w]
                    )
                else:
                    dp[i][w] = dp[i - 1][w]

        selected_packages = []
        w_remaining = w_max
        for i in range(n, 0 , -1):
            if dp[i][w_remaining] != dp[i - 1][w_remaining]:
                pack = packages[i-1]
                selected_packages.append(pack)
                w_remaining -= pack.weight

        return {
            "max_value": dp[n][w_max],
            "total_weight": w_max - w_remaining,
            "selected_items": selected_packages
        }
                

    def optimize_greedy(self, packages: list[Package], container: Container) -> dict:
        """
        aqui resolvemos el problema de la mochila usando un enfoque voraz (greedy)
        0(n log n) debido al ordenamiento inicial
        """
        sorted_packages = sorted(packages, key=lambda p: p.value / p.weight, reverse=True)

        selected_packages = []
        current_weight = 0
        total_value = 0

        for pack in sorted_packages:
            if current_weight + pack.weight <= container.max_weight:
                selected_packages.append(pack)
                current_weight += pack.weight
                total_value += pack.value

        return {
            "max_value": total_value,
            "total_weight": current_weight,
            "selected_items": selected_packages
        }

