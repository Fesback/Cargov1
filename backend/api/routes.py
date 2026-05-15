from fastapi import APIRouter, HTTPException
from core.models import Package, Container
from services.algorithm_service import AlgorithmService
import traceback

router = APIRouter()
service = AlgorithmService()

@router.post("/optimize")
def optimize_cargo(payload: dict):
    try:
        packages = [Package(**p) for p in payload["packages"]]
        container_obj = Container(max_weight=payload["capacity"])

        dp_result = service.optimize_dynamic_programing(packages, container_obj)
        greedy_result = service.optimize_greedy(packages, container_obj)

        return {
            "dynamic_programming": {
                "value": dp_result["max_value"],
                "weight": dp_result["total_weight"],
                "items": [p.__dict__ for p in dp_result["selected_items"]],
                "complexity": "O(n * W)"
            },
            "greedy": {
                "value": greedy_result["max_value"],
                "weight": greedy_result["total_weight"],
                "items": [p.__dict__ for p in greedy_result["selected_items"]],
                "complexity": "O(n log n)"
            }
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))