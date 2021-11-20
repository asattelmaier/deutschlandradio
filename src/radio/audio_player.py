class AudioPlayer:
    def __init__(self, player, player_state):
        self._player = player
        self._player_state = player_state

    @staticmethod
    def create(g_streamer):
        g_streamer.init(None)
        player = g_streamer.ElementFactory.make("playbin", "player")

        return AudioPlayer(player, g_streamer.State)

    @property
    def is_playing(self):
        current_state = self._player.current_state

        return current_state is self._player_state.PLAYING

    def set_uri(self, uri):
        self._player.set_property('uri', uri)

    def play(self):
        self._player.set_state(self._player_state.PLAYING)

    def stop(self):
        self._player.set_state(self._player_state.NULL)
