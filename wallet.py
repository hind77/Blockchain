#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:05:35 2021

@author: mac
"""


import binascii
from Crypto import Random
from Crypto.PublicKey import RSA

class Wallet:
    
    def __init__(self):
        
        self.private_key = None
        self.public_key = None
        
    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key 
        
    def load_keys(self):
        pass
        
    def generate_keys(self):
        r = Random.new()
        private_key = RSA.generate(1024, r.read)
        public_key = private_key.publickey()
        return ((binascii.hexlify(private_key.exportKey(format='DER'))).decode('ascii'),
                (binascii.hexlify(public_key.exportKey(format='DER'))).decode('ascii'))
                
        