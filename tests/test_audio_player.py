import unittest

from audio_player.audio_player import AudioPlayer
from unittest.mock import MagicMock


class TestAudioPlayer(unittest.TestCase):
    def test_creation(self):
        """
        Test that a AudioPlayer instance will be created.
        """
        g_streamer = MagicMock()

        audio_player = AudioPlayer.create(g_streamer)

        self.assertIsInstance(audio_player, AudioPlayer)

    def test_change_channel(self):
        """
        Test that the GStreamer created players URI will be set.
        """
        g_streamer = MagicMock()
        player = MagicMock()

        g_streamer.ElementFactory.make.return_value = player
        audio_player = AudioPlayer.create(g_streamer)
        audio_player.change_channel('https://some-uri')

        player.set_property.assert_called_with('uri', 'https://some-uri')

    def test_play(self):
        """
        Test that the GStreamer player state will be set to "Playing".
        """
        g_streamer = MagicMock()
        player = MagicMock()

        g_streamer.State.PLAYING = "PLAYING"
        g_streamer.ElementFactory.make.return_value = player
        audio_player = AudioPlayer.create(g_streamer)
        audio_player.play()

        player.set_state.assert_called_with("PLAYING")

    def test_stop(self):
        """
        Test that the GStreamer player state will be set to "NULL".
        """
        g_streamer = MagicMock()
        player = MagicMock()

        g_streamer.State.NULL = "NULL"
        g_streamer.ElementFactory.make.return_value = player
        audio_player = AudioPlayer.create(g_streamer)
        audio_player.stop()

        player.set_state.assert_called_with("NULL")
