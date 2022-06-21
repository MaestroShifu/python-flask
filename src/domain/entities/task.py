from datetime import datetime

class Task:
    def __init__(self, 
        description: str,
        title: str,
        start_date: datetime,
        end_date: datetime
    ):
        self.description = description
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
