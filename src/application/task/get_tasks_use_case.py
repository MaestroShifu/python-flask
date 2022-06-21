from domain.contracts.task_contract import TaskContract

class GetTasksUseCase(object):
    def __init__(self, tastContract: TaskContract):
        self.tastContract = tastContract
    
    def execute(self):
        self.tastContract.get()
