class TodoItem:
    def __init__(self, description):
        self.__description = description
        self.__done = False

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def is_done(self):
        return self.__done

    def mark_as_done(self):
        self.__done = True


class TodoList:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def get_items(self):
        return self.__items

    def get_pending_items(self):
        return [item for item in self.__items if not item.is_done()]

    def get_done_items(self):
        return [item for item in self.__items if item.is_done()]

    def mark_item_as_done(self, item):
        item.mark_as_done()
