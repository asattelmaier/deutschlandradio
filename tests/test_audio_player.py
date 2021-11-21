import unittest
from unittest.mock import MagicMock

from src.radio import AudioPlayer


class TestAudioPlayer(unittest.TestCase):
    def test_creation(self):
        """
        Test that a AudioPlayer instance will be created.
        """
        g_streamer = MagicMock()

        audio_player = AudioPlayer.create(g_streamer)

        self.assertIsInstance(audio_player, AudioPlayer)

    def test_set_uri(self):
        """
        Test that the GStreamer created players URI will be set.
        """
        g_streamer = MagicMock()
        player = MagicMock()

        g_streamer.ElementFactory.make.return_value = player
        audio_player = AudioPlayer.create(g_streamer)
        audio_player.set_uri('https://some-uri')

        player.set_property.assert_called_once_with('uri', 'https://some-uri')

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

        player.set_state.assert_called_once_with('PLAYING')

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

        player.set_state.assert_called_once_with('NULL')

    def test_is_playing(self):
        """
        Test is playing, if the current state equals "PLAYING".
        """
        g_streamer = MagicMock()
        player = MagicMock()

        g_streamer.State.PLAYING = 'PLAYING'
        g_streamer.ElementFactory.make.return_value = player
        player.current_state = 'PLAYING'
        audio_player = AudioPlayer.create(g_streamer)

        self.assertTrue(audio_player.is_playing)

    def test_is_not_playing(self):
        """
        Test is not playing, if the current state not equals "PLAYING".
        """
        g_streamer = MagicMock()
        player = MagicMock()

        g_streamer.State.PLAYING = 'PLAYING'
        g_streamer.ElementFactory.make.return_value = player
        player.current_state = 'NULL'
        audio_player = AudioPlayer.create(g_streamer)

        self.assertFalse(audio_player.is_playing)
