import os
from g_object import AppIndicator

NAME = 'rundfunk'
ICON = os.path.dirname(os.path.realpath(__file__)) + "/assets/rundfunk-app-icon.svg"
CATEGORY = AppIndicator.IndicatorCategory.APPLICATION_STATUS
