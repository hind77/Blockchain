#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Hindou
"""

import json
import hashlib

def hash_string(string):
    
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    
    '''
    This function hash a given block
    
    iputs:
        block: the current block
        
    ''' 
    valid_block = block.__dict__.copy()
    valid_block['transactions'] = [trans.order() for trans in valid_block['transactions']]
    return hash_string(json.dumps(valid_block, sort_keys=True).encode())