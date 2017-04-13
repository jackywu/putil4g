#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: fileencoding=utf-8 autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import unittest
from putil4g.transition import Transition

class TestTransition(unittest.TestCase):

    def test_complete_dna(self):
        desired_value = 'TGACTAGCTAATGCATATCATAAACGATAGTATGTATATATAGCTACGCAAGTA'

        my_dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
        result = Transition().complete_dna(my_dna)

        self.assertEqual(desired_value, result)



