#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Hindou
"""
from helpers.hash_util import hash_string, hash_block
class Validation:
    
    @classmethod
    def verify_chain(cls, blockchain):    
        '''
        This function verifies the hash of the previous block hash with the hash provided in the current block
        '''      
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.pre_hash != hash_block(blockchain[index-1]):
                return False
            if not cls.correct_structure_of_proof(block.transactions[:-1], block.pre_hash, block.nonce):
                print("invalid proof of work")
                return False
        return True
    
    @classmethod
    def verify_transactions(cls, transactions, get_balance):
        return all([cls.verify_transaction(trans, get_balance) for trans in transactions])
    
    @staticmethod
    def verify_transaction(transaction, get_balance):
    
        '''
        This function verify if the sender can make the transaction 
        using is actual balance 
        
        iputs:
            transaction: the current transaction
        '''  
        sender_balance = get_balance()
        return sender_balance >= transaction.amount  
    
    @staticmethod
    def correct_structure_of_proof(transactions, previous_hash,
                  nonce):
        '''
        This function provides proof condition results over the proof of work 
        
        inputs:
            transactions: list of the transactions
            previous_hash: the hash of the previous block
            nonce: the proof of work nonce
        '''
        proof = (str([trans.order() for trans in transactions]) + str(previous_hash) + str(nonce)).encode()
        proof_hash = hash_string(proof)
        return proof_hash[0:2] == '00'