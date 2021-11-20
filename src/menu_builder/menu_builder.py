class MenuBuilder:
    def __init__(self, menu, item_factory):
        self._menu = menu
        self._item_factory = item_factory

    @staticmethod
    def create(menu_factory, item_factory):
        menu = menu_factory()

        return MenuBuilder(menu, item_factory)

    def add_item(self, label, handler):
        item = self._item_factory(label)
        item.connect('activate', handler)

        self._menu.append(item)

        return self

    def build(self):
        self._menu.show_all()

        return self._menu
