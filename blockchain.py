#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Hindou 
"""

import functools
import hashlib
import json
import pickle


from helpers.hash_util import hash_block
from block import Block
from transaction import Transaction
from helpers.validation import Validation

REWARD = 10


class Blockchain:
    
    def __init__(self, node_id):
        init_block = Block(0, '', [], 100, 0)
        self.__chain = [init_block]
        self.__transactions = []
        self.load_blockchain_and_transactions()
        self.node_id = node_id
        
    def get_chain(self):
        return self.__chain[:]
    def get_transactions(self):
        return self.__transactions[:]

    def load_blockchain_and_transactions(self):
        try:
            with open('blockchain.txt', mode='r') as f:
                # data = pickle.loads(f.read())
                data = f.readlines()

                # blockchain = data['blockchain']
                # transactions = data['transactions']
                blockchain= json.loads(data[0][:-1])
                updated_blockchain = []
                for block in blockchain:
                    trans = [Transaction(trans['sender'], trans['receiver'], trans['amount']) for trans in block['transactions']]
                    updated_block = Block(block['index'], block['pre_hash'], trans,block['nonce'], block['timestamp'])
                    updated_blockchain.append(updated_block)
                self.__chain = updated_blockchain
                self.__transactions= json.loads(data[1])
                updated_transactions = []
                for trans in self.__transactions:
                    updated_trans = Transaction(trans['sender'], trans['receiver'], trans['amount'])
                    updated_transactions.append(updated_trans)
                transactions = updated_transactions
        except (IOError, IndexError):
            pass

    def save_blockchain_and_transactions(self):
        try:
            with open('blockchain.txt', mode='w') as f:
                valid_blockchain = [block.__dict__ for block in [Block(block_s.index,block_s.pre_hash, [trans.__dict__ for trans  in block_s.transactions] ,block_s.nonce, block_s.timestamp) for block_s in self.__chain]]
                valid_transaction = [trans.__dict__ for trans in self.__transactions]
                f.write(json.dumps(valid_blockchain))
                f.write('\n')
                f.write(json.dumps(valid_transaction))
                # data = {'blockchain': blockchain,
                #         'transactions': transactions}
                # f.write(pickle.dumps(data))
        except IOError:
            print(" saving failed")
            
    def proof_of_work(self):
        
        '''
        This function tests over the nonce value as a proof of work 
        '''      
        previous_block = self.__chain[-1]
        previous_hash = hash_block(previous_block)
        nonce = 0
        
        while not Validation.correct_structure_of_proof(self.__transactions, previous_hash,nonce):
            nonce += 1
        return nonce

    def get_balance(self):
        
        '''
        This function returns the balance of a specific user
        
        iputs:
            user: a given participant 
        '''  
        user = self. node_id
        amounts_sender = [[trans.amount for trans in block.transactions
                      if trans.sender == user] for block in self.__chain]
        
        transaction_sender = [trans.amount
                          for trans in self.__transactions if trans.sender == user]
        
        transaction_sender = [trans.amount for trans in self.__transactions if trans.sender == user ]
        
        amounts_sender.append(transaction_sender)
        balance_sent = functools.reduce(lambda trans_sum, trans_amount: trans_sum + sum(trans_amount) if len(trans_amount)> 0 else trans_sum + 0,
                                        amounts_sender, 0)
    
        amounts_receiver = [[x.amount for x in block.transactions if x.receiver == user] for block in self.__chain]
        balance_received = functools.reduce(lambda trans_sum, trans_amount: trans_sum+ sum(trans_amount)  if len(trans_amount)> 0 else trans_sum + 0,
                                        amounts_receiver, 0)
        return balance_received - balance_sent           

    def add_transaction(self, receiver,sender, amount = 0.1):
        
        '''
        This function add a new value to the blockchain
        
        iputs:
            sender: the coins' sender
            receiver: the coins' receiver
            amount: coins amount 
        '''  
        # transaction = {'sender':sender, 
        #                'receiver':receiver, 
        #                'amount':amount}
        if self.node_id == None:
            return False
        transaction = Transaction(sender, receiver, amount)
        if Validation.verify_transaction(transaction, self.get_balance):
            self.__transactions.append(transaction)
            # users.add(sender)
            # users.add(receiver)
            self.save_blockchain_and_transactions()
            return True
        return False

        
    def show_transactions(self):
        print("these are the transactions:", self.__transactions)
    

    
    def mine_block(self):
        
        '''
        This function add the curent block to the blockchain
        ''' 
        if self.node_id == None:
            return False
        previous_block = self.__chain[-1]
        block_hash = hash_block(previous_block)
        proof = self.proof_of_work()
        # reward = {'sender': 'MINING_APP',
        #      'receiver':owner,
        #      'amount': REWARD 
        #      }
        reward = Transaction('MINING_APP', self.node_id, REWARD)
        transaction_copy = self.__transactions[:]
        transaction_copy.append(reward)
        block = Block(len(self.__chain), block_hash, transaction_copy, proof )
        self.__chain.append(block)
        self.__transactions = []
        self.save_blockchain_and_transactions()
        
        return True 
    
    def last_blockchain_value(self):
        
        '''
        This function returns the last value of the blockchain 
        '''
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]







    

    







        



        

            
    
        