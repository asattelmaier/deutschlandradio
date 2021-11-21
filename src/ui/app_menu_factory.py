class AppMenuFactory:
    def __init__(self, menu_builder, radio, channel, quit_handler):
        self._menu_builder = menu_builder
        self._radio = radio
        self._channel = channel
        self._quit_handler = quit_handler

    def create(self):
        return self._build_menu()

    def _build_menu(self):
        return self._menu_builder \
            .add_item('Deutschlandfunk', self._create_deutschlandfunk_item_handler()) \
            .add_item('Deutschlandfunk Kultur', self._create_deutschlandfunk_kultur_item_handler()) \
            .add_item('Deutschlandfunk Nova', self._create_deutschlandfunk_nova_item_handler()) \
            .add_item('Dokumente und Debatten', self._create_dokumente_und_debatten_item_handler()) \
            .add_separator() \
            .add_item('Schließen', self._quit_handler) \
            .build()

    def _create_deutschlandfunk_item_handler(self):
        return self._create_channel_item_handler(self._channel.DEUTSCHLANDFUNK)

    def _create_deutschlandfunk_kultur_item_handler(self):
        return self._create_channel_item_handler(self._channel.DEUTSCHLANDFUNK_KULTUR)

    def _create_deutschlandfunk_nova_item_handler(self):
        return self._create_channel_item_handler(self._channel.DEUTSCHLANDFUNK_NOVA)

    def _create_dokumente_und_debatten_item_handler(self):
        return self._create_channel_item_handler(self._channel.DOKUMENTE_UND_DEBATTEN)

    def _create_channel_item_handler(self, channel):
        return lambda _: self._radio.update_channel(channel)
