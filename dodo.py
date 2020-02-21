# -*- coding: utf-8 -*-
'''
doit utility::

Do this after having changed an RST file.
Start this from chcko-x/chcko/::

    $ doit -kd. html

Do this after having changed the header (path, kind, level) in a html or rst file::

    $ doit initdb

Do this after any changes, especially in the main code::

    $ doit test
    $ doit cov

Do this to add new content, html or rst::

    $ doit -kd. new
    $ doit -kd. rst

task_included is internal.

'''

import sys
import os

chckouninstalled = os.path.normpath(os.path.join(os.path.dirname(__file__),'..','chcko'))
if os.path.exists(chckouninstalled):
    sys.path.insert(0,chckouninstalled)

from chcko.chcko import doit_tasks

doit_tasks.set_base(__file__)

task_included = doit_tasks.task_included
task_html = doit_tasks.task_html
task_initdb = doit_tasks.task_initdb
