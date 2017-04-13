#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: fileencoding=utf-8 autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

from .base import *

class Transition():

    BASE_MAP = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    def complete_dna(self, dna_seq):
        if not isinstance(dna_seq, str):
            raise Putil4gException("dna_seq is not text sequence")

        result = []
        for i in dna_seq:
            result.append(self.BASE_MAP.get(i.upper()))

        return ''.join(result)



