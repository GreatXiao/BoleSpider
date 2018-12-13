#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-02 17:38:47
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "pyart"])