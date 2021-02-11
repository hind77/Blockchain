#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Hindou

"""

from blockchain import Blockchain
from uuid import uuid4
from helpers.validation import Validation
from wallet import Wallet

class Node:
    
    def __init__(self):
        #self.wallet.public_key = str(uuid4())
        self.wallet = Wallet()
        self.blockchain = None
        
    
    def get_user_transaction(self):
    
        '''
        This function returns the user input value (float) 
        '''
        receiver = input("Please input the ID of the receiver: ")
        coins_amount = float(input("Please input the amount of your transaction: "))
        return receiver, coins_amount
    
    def get_user_choice(self):
        return input("Your choice: ")

    def show_blockchain(self):
        for block in self.blockchain.get_chain():
            print("This is the output block")
            print(block)
     
        print("*" * 20)
        
    def get_the_input(self):
        run = True 
        while run:
            print("Define your choice:")
            print("1: Add a transaction")
            print("2: Mine the block")
            print("3: Show the blockchain")
            print("4: Verify the transactions validity")
            print("5: Create wallet")
            print("6: Load wallet")
            print("q: Quit")
            choice = self.get_user_choice()
            if choice == '1':
                receiver, amount = self.get_user_transaction()
                if self.blockchain.add_transaction(receiver, self.wallet.public_key, amount= amount):
                    print("transaction succefuly added")
                else:
                    print("transaction failed")
                self.blockchain.show_transactions()
            elif choice == '2':                
                if not self.blockchain.mine_block():
                    print("miming failed no wallet is found")

            elif choice == '3':
                self.show_blockchain()
            elif choice == '4':
                Validation.verify_transactions(self.blockchain.get_transactions(), self.blockchain.get_balance) 
            elif choice == '5':               
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif choice == '6':
                pass
            elif choice == 'q':
                run = False
            else:
                print("invalid input")
            
            if not Validation.verify_chain(self.blockchain.get_chain()):
                print("Invalid blockchain")
                break
            3
            print('Balance of {}: {:6.2f}'.format(self.wallet.public_key, self.blockchain.get_balance()))
        else: 
            print("End!")
            
if __name__ == '__main__':            
    node = Node()
    node.get_the_input()