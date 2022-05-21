from curses.ascii import isdigit
import json
import managejson
from datetime import datetime
class Wallet:
    def __init__(self,username):
        self.username = username
        self.all_casino_data = managejson.get_dictionary('casino')
        self.all_capitals_data = managejson.get_dictionary('capitals')
        
        if self.is_account_exist() == True:#if the account is exist
            self.capital = self.get_capital_from_json()
            
        else:
            
            self.capital = float(0)
            self.update_json(float(0))

    def is_account_exist(self):
        j= self.get_dictionary()
        if self.username in j.keys():
            return True
        else:
            return False 
        
    def get_capital_from_json(self):
        '''it returns capital'''
        j= managejson.get_dictionary('capitals')
        try:
            j[self.username]  
            return j[self.username]
        except:
            return False
    
    def player_Won_save_in_(self,amount_of_money):
        date = datetime.datetime.now()
        self.capital += amount_of_money
        
        #manuplating data
        self.all_casino_data[self.username]['win'][date]=amount_of_money
        self.all_casino_data[self.username]['total'] = self.capital
        
        self.all_capitals_data[self.username]=self.capital 
        
        #saving data
        managejson.save_dictionary(self.all_casino_data,'casino')
        managejson.save_dictionary(self.all_capitals_data,'capitals')
        
    def player_lost_save_in_(self,amount_of_money):
        date = datetime.datetime.now()
        self.capital -= amount_of_money
        
        #manuplating data
        self.all_casino_data[self.username]['lose'][date]=amount_of_money
        self.all_casino_data[self.username]['total'] = self.capital
        
        self.all_capitals_data[self.username]=self.capital 
        
        #saving data
        managejson.save_dictionary(self.all_casino_data,'casino')
        managejson.save_dictionary(self.all_capitals_data,'capitals')
        
    def upload_money_into_wallet(self):
        '''that function use player won function in itself'''
        correct_input  = False
        while correct_input == False:
            uploadable_money = input('enter amount of money to upload')
            if isdigit(uploadable_money)==True:
                self.player_Won_save_in_(uploadable_money)
    
    
    
    
    
    
