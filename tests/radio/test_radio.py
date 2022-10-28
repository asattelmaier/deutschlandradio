import unittest
from unittest.mock import MagicMock

from src.radio import Radio


class TestRadio(unittest.TestCase):
    def test_current_channel(self):
        """
        Test that the current channel will be set.
        """
        audio_player = MagicMock()
        event_bus = MagicMock()
        channel = MagicMock()

        channel.value = 'some-channel'
        audio_player.is_playing = True
        Radio.create(audio_player, event_bus, channel)

        audio_player.set_uri.assert_called_once_with('some-channel')
