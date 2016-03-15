# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:13:45 2016

@author: narf
"""

class Customer:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        if (amount > self.balance):
            print "Your balance is now negative."
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
        
    def showBalance(self):
        print "Your balance is %d" % self.balance
        

myCustomer = Customer("Tim", 1000)
myCustomer.showBalance()
myCustomer.withdraw(2000)
myCustomer.showBalance()
myCustomer.deposit(10000000)
myCustomer.showBalance()