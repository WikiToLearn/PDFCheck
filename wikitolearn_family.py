# -*- coding: utf-8 -*-
"""
This family file was auto-generated by $Id: b4675f8c1426906ff25dbf5dc703facd391360da $
Configuration parameters:
  url = http://it.wikitolearn.org/
  name = wikitolearn

Please do not commit this to the Git repository!
"""

from pywikibot import family
from pywikibot.tools import deprecated


class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikitolearn'
        self.langs = {
            'it': 'it.wikitolearn.org',
            'en': 'en.wikitolearn.org',
            'devit': 'it.wikitolearn.vodka',
            'deven': 'en.wikitolearn.vodka',
            'localit': 'en.tuttorotto.biz',
            'localen': 'en.tuttorotto.biz',
        }

    def scriptpath(self, code):
        return {
            'it': '',
            'en': '',
            'devit': '',
            'deven': '',
            'localit': '',
            'localen': '',
        }[code]

    @deprecated('APISite.version()')
    def version(self, code):
        return {
            'it': u'1.25.2',
            'en': u'1.25.2',
            'devit': u'1.25.2',
            'deven': u'1.25.2',
            'localit': u'1.25.2',
            'localen': u'1.25.2',
        }[code]

    def protocol(self, code):
        return {
            'it': u'http',
            'en': u'http',
            'devit': u'http',
            'deven': u'http',
            'localit': u'http',
            'localen': u'http',
        }[code]
