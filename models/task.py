from datetime import datetime

class Task:
    def __init__(self, user_id, text, urgent, important, task_id=None, done=False,
                created_at=None, done_at=None):
        self.id = task_id if task_id is not None else id(self)
        self.user_id = user_id
        self.text = text
        self.urgent = urgent
        self.important = important
        self.done = done
        self.created_at = created_at if created_at is not None else datetime.now()
        self.done_at = done_at

    def quadrant(self):
        if self.urgent and self.important:
            return 1
        elif not self.urgent and self.important:
            return 2
        elif self.urgent and not self.important:
            return 3
        else:
            return 4
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "text": self.text,
            "urgent": self.urgent,
            "important": self.important,
            "done": self.done,
            "created_at":self.created_at.isoformat(),
            "done_at": self.done_at.isoformat() if self.done_at else None,
        }