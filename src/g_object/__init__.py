import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gst', '1.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as GimpToolkit
from gi.repository import AppIndicator3 as AppIndicator
from gi.repository import Gst as GStreamer
from gi.repository.Gst import State
from gi.overrides.Gtk import Menu
from gi.repository.Gtk import CheckMenuItem
