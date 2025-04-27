import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.tasks import load_tasks, save_tasks, filter_tasks_by_priority, filter_tasks_by_category

TEST_FILE = "test_tasks.json"

@pytest.fixture
def sample_tasks():
    return [
        {"id": 1, "title": "Task 1", "priority": "High", "category": "Work", "completed": False},
        {"id": 2, "title": "Task 2", "priority": "Low", "category": "Personal", "completed": True},
        {"id": 3, "title": "Task 3", "priority": "Medium", "category": "School", "completed": False},
    ]

def test_save_and_load_tasks(sample_tasks):
    save_tasks(sample_tasks, file_path=TEST_FILE)
    loaded_tasks = load_tasks(file_path=TEST_FILE)
    assert loaded_tasks == sample_tasks
    os.remove(TEST_FILE)

def test_filter_tasks_by_priority(sample_tasks):
    high_priority = filter_tasks_by_priority(sample_tasks, "High")
    assert len(high_priority) == 1
    assert high_priority[0]["title"] == "Task 1"

def test_filter_tasks_by_category(sample_tasks):
    personal_tasks = filter_tasks_by_category(sample_tasks, "Personal")
    assert len(personal_tasks) == 1
    assert personal_tasks[0]["title"] == "Task 2"