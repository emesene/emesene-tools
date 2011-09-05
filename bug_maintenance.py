#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from launchpadlib.launchpad import Launchpad
import os

cachedir = os.path.expanduser("~/.launchpadlib/")
launchpad = Launchpad.login_with('emesene bug maintenance', 'production', cachedir)
ubuntu = launchpad.distributions['ubuntu']
emesene = ubuntu.getSourcePackage(name='emesene')
tasks = emesene.getBugTasks()
for task in tasks:
    if task.date_created.year < 2011 and task.status in ('New', 'Confirmed'):
        print task.title
        bug = task.bug
        task.status = u'Invalid'
        task.lp_save()
        bug.newMessage(content='emesene 1.x is not supported anymore. Please use emesene 2, which is available in from the standard repositories since Natty, or from our ppa:\n https://launchpad.net/~emesene-team/+archive/emesene-stable\n\nIf you run into any bugs with emesene 2, please report them at\nhttps://github.com/emesene/emesene/issues')
