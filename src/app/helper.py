from browser import window, document


class Event:
    """
    Simple Event Class
    """
    def __init__(self):
        self.listeners = []

    def subscribe(self, handler) -> None:
        """
        Subscribe to an event
        :param handler: Handler that will be fired
        :return: None
        """
        self.listeners.append(handler)

    def fire(self, data) -> None:
        """
        broadcast data to all listener
        :param data: Data that will be broadcasted
        :return: None
        """
        for i in self.listeners:
            i(data)


def print_error(msg) -> None:
    """
    print error message
    :param msg: message that will be printed
    :return: None
    """
    print("error: ", msg)


def register_submit(class_name, fire) -> None:
    """
    Register on a form a handler
    :param class_name: class name of the form
    :param fire: function that will be fire on form submit
    :return: None
    """
    def submit_handler(event) -> None:
        """
        Handle form submit and fire handler
        :param event: Default html form object
        :return: None
        """
        event.preventDefault()
        fire()

    if window.jQuery('.' + class_name).length == 1:
        return window.jQuery('.' + class_name).on('submit', submit_handler)


def elm(elm_type: object, attr=None) -> any:
    """
    Create an HTML element with given type and attribute
    :param elm_type: type of the element
    :param attr: attributes that will given to the element
    :return: jQuery HTML element
    """
    jquery_elm = window.jQuery(document.createElement(elm_type))
    if attr is not None:
        jquery_elm.attr(attr)
    return jquery_elm


def div(class_name) -> any:
    """
    Create a jquery div with given class attribute/string
    :param class_name: class name of the element
    :return: jQuery HTML element
    """
    return elm('div', {'class': class_name})
