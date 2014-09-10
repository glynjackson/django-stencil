# -*- coding: utf-8 -*-
import sys

from .settingsBase import *
from .logging import *
from .settingsEmail import *
from .settingsUsers import *

if sys.argv[1] == 'runserver' or sys.argv[1] == 'migrate':
    from .settingsDevelopment import *
else:
    from .settingsProduction import *
