class Task:
    """
    Task with basic information
    """
    def __init__(self, task_id: int, name: str, priority: int, description: str):
        """
        :param task_id: Id of the task
        :param name: Name of the task
        :param priority: Priority of the task. Starting with 1 as highest priority
        :param description: Description of the task
        """
        self.task_id: int = task_id
        self.name: str = name
        self.priority: int = priority
        self.description: str = description


class TaskModel:
    def __init__(self, tasks=None):
        """
        :param tasks: Optional tasks that will be added to the model
        """
        if tasks is None:
            tasks = []
        self.tasks: [Task] = tasks
        self.counter = len(tasks)

    def task_add(self, name: str, priority, description) -> None:
        """
        Add a task
        :param name: Name of the task
        :param priority: Priority of the task. Starting with 1 as highest priority
        :param description: Description of the task
        :return: None
        """
        self.tasks.append(Task(self.counter, name, priority, description))
        self.counter += 1
