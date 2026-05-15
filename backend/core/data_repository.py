import json
import os
from core.models import Package

class PackageRepository:
    def get_all_packages(self) -> list[Package]:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "data", "packages_mock.json")

        with open(file_path, "r", encoding="uft-8") as file:
            data =  json.load(file)

        return [Package(**item) for item in data]