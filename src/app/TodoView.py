from browser import window
from typing import List

from TodoModel import Task
from helper import register_submit, div, elm
import html


class ElementFactoryTask:
    def __init__(self, task: Task):
        """
        Tasks of the element
        :param task: Task data
        """
        self.task = task

    def delete_task(self, *e) -> None:
        """
        Handler for deleting tasks
        :param e: jQuery parameter
        :return: None
        """
        print("modal_delete not implemented")

    def get(self) -> any:
        """
        Get HTML element of the task
        :return: jQuery HTML element
        """
        return div('card task-id-' + str(self.task.task_id)).append(
            div('card-body').append(
                div('row').append(
                    div('col-4').append(elm('h1').text(self.task.name)),
                    div('col-6').append(elm('h1').text(self.task.description)),
                    div('col-2').append(
                        elm('h1').append(
                            elm('a', {'href': 'javascript:void(0)'}).text('delete').click(self.delete_task)
                        )
                    )
                )
            )
        )


class TodoView:
    def __init__(self, controller):
        """
        :param controller: TodoApp controller
        """
        self.controller = controller
        register_submit('form-todo-add', self.form_task_add)
        self.controller.event_task_add.subscribe(self.task_on_add)
        self.todo_list_elm = window.jQuery('.todo-list')

    def form_task_add(self) -> None:
        """
        Handler that will be fired on form submit
        :return: None
        """
        self.controller.task_add(
            html.escape(window.jQuery('.input-todo-task')[0].value),
            int(window.jQuery('.select-todo-priority')[0].value),
            html.escape("")
        )
        window.jQuery('.input-todo-task')[0].value = ''

    def task_on_add(self, tasks: List[Task]) -> None:
        """
        Add task to the view
        :param tasks: List of Tasks
        :return: None
        """
        self.todo_list_elm.empty()
        for task in tasks:
            self.todo_list_elm.append(ElementFactoryTask(task).get())
