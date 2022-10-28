from gi.repository.Gst import State


class Playbin:
    """
    Reverse engineered GStreamer playbin class.

    Further reading: https://gstreamer.freedesktop.org/documentation/playback/playbin.html?gi-language=c
    """

    current_state: State

    def set_state(self, state: State) -> None:
        pass

    def set_property(self, name: str, value: str) -> None:
        pass
