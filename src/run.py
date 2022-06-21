from flask import Flask
from application.task.get_tasks_use_case import GetTasksUseCase
from domain.contracts.task_contract import TaskContract

from infrastructure.config import Config

app: Flask = Flask(__name__)

""" Example clean architecture """
class TestExample(TaskContract):
    def __init__(self):
        super().__init__()
    def get(self) -> None:
        print('Funciono!!')

@app.route('/')
def hello_world():
    useCase = GetTasksUseCase(tastContract=TestExample())
    useCase.execute()
    return Config.TEST_URL or 'Hello world'
