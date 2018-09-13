# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

try:
	print sys.argv
except ValueError:
	print "Not a number!"