# -*- coding: utf-8 -*-

import re

target = ["/leader/2320"]

#regex = u'//(?P<skill>[\w]+)//(?P<num>[\d]+)'
regex = u'([\d]+)'
match = re.search(regex, target[0], re.U)
print match.group()
#skill = match.group('skill')
#skill_no = match.group('num')
