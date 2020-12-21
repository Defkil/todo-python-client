from TodoController import TodoController
from TodoView import TodoView


def run() -> None:
    """
    Create controller and view
    :return: None
    """
    controller = TodoController()
    view = TodoView(controller)
