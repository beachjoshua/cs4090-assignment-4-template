import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.tasks import get_overdue_tasks
from datetime import datetime, timedelta

def test_get_overdue_tasks():
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    tasks = [
        {"id": 1, "title": "Old Task", "due_date": yesterday, "completed": False},
        {"id": 2, "title": "Future Task", "due_date": tomorrow, "completed": False},
        {"id": 3, "title": "Completed Old Task", "due_date": yesterday, "completed": True},
    ]
    
    overdue = get_overdue_tasks(tasks)
    assert len(overdue) == 1
    assert overdue[0]["title"] == "Old Task"