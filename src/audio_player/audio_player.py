class AudioPlayer:
    def __init__(self, player, player_state):
        self._player = player
        self._player_state = player_state

    @staticmethod
    def create(g_streamer):
        g_streamer.init(None)
        player = g_streamer.ElementFactory.make("playbin", "player")

        return AudioPlayer(player, g_streamer.State)

    def change_channel(self, uri):
        self._player.set_property('uri', uri)

    def play(self):
        self._player.set_state(self._player_state.PLAYING)

    def stop(self):
        self._player.set_state(self._player_state.NULL)
