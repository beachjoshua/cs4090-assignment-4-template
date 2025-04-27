import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.tasks import filter_tasks_by_completion, search_tasks

@pytest.fixture
def task_list():
    return [
        {"id": 1, "title": "Buy milk", "description": "Buy 2 liters of milk", "completed": False},
        {"id": 2, "title": "Study", "description": "Study for math exam", "completed": True},
        {"id": 3, "title": "Workout", "description": "Leg day", "completed": False},
    ]

@pytest.mark.parametrize("completed, expected_count", [
    (True, 1),
    (False, 2)
])
def test_filter_tasks_by_completion(task_list, completed, expected_count):
    filtered = filter_tasks_by_completion(task_list, completed)
    assert len(filtered) == expected_count

@pytest.mark.parametrize("query, expected_titles", [
    ("milk", ["Buy milk"]),
    ("study", ["Study"]),
    ("day", ["Workout"]),
])
def test_search_tasks(task_list, query, expected_titles):
    results = search_tasks(task_list, query)
    titles = [task["title"] for task in results]
    assert titles == expected_titles