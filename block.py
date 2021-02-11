#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Hindou

"""
from time import time
from helpers.printing import Printing


class Block(Printing):
    
    def __init__(self, index, pre_hash, transactions, nonce, time= time()):
        self.index = index
        self.pre_hash = pre_hash
        self.transactions = transactions
        self.timestamp = time
        self.nonce = nonce
        

        