#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Hindou
"""
from collections import OrderedDict
from helpers.printing import Printing

class Transaction(Printing):
    
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        

        
    def order(self):
        return OrderedDict([('sender', self.sender), ('receiver', self.receiver), ('amount', self.amount)])