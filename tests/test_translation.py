#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: fileencoding=utf-8 autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import unittest
from putil4g.translation import Translation

class TestTranslation(unittest.TestCase):

    def test_translate_dna(self):
        t = Translation()
        # input sequence is easy
        self.assertEqual(t.translate_dna("ATGTTCGGT"), "MFG")

        # input sequence has incomplete codons at the end
        self.assertEqual(t.translate_dna("ATCGATCGAT"), "IDR")

        # input sequence contains N
        self.assertEqual(t.translate_dna("ACGANCGAT"), "T*D")
