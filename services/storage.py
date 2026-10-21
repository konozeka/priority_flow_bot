from models.task import Task

_storage = {}

def add_task(user_id: int, text: str, urgent: bool, important: bool) -> Task:
    new_task= Task(user_id=user_id, text=text, urgent=urgent, important=important)

    if user_id not in _storage:
        _storage[user_id] = []

    _storage[user_id].append(new_task)
    return new_task

def get_user_tasks(user_id: int) -> list[Task]:
    return _storage.get(user_id, [])

def get_tasks_by_quadrant(user_id: int, quadrant: int) -> list[Task]:
    user_tasks = get_user_tasks(user_id)
    return [task for task in user_tasks if task.quadrant() == quadrant and not task.done]

def mark_task_done(user_id: int, task_id: int) -> bool:
    user_tasks = get_user_tasks(user_id)
    for task in user_tasks:
        if task.id == task_id:
            task.done = True
            return True
    return False
