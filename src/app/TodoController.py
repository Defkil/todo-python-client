from helper import Event, print_error
from TodoModel import TaskModel


class TodoController:
    """
    Main controller for handling the TodoApp
    """
    def __init__(self):
        self.taskModel = TaskModel()
        self.event_task_add = Event()

    def task_add(self, task: str, priority: int, description: str) -> None:
        """
        Add a task
        :param task: Task Name
        :param priority: Priority of the task. Starting with 1 as highest priority
        :param description: Task description
        :return: None
        """
        if len(task) == 0:
            return print_error("No Task")
        if not -1 < priority < 4:
            return print_error("Selected priority dont exist")

        task = self.taskModel.task_add(task, priority, description)
        self.event_task_add.fire(self.taskModel.tasks)
