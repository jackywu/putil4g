#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: fileencoding=utf-8 autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import unittest

def main():
    discover = unittest.defaultTestLoader.discover('./tests', pattern='test*.py')
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(discover)

if __name__ == '__main__':
    main()


