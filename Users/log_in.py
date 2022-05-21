import sys
import json
import managejson
from Users.loginfunctions import exit_question, is_nick_exist
import loginfunctions
from Users.addresses import Address
from Users.wallet import Wallet
class LogIn:
    def __init__(self):


        ###desicion taking time y or n
        self.usersdesicion = self.have_u_got_account()
        if self.usersdesicion ==True:
            
            self.username=self.taking_username()
            while self.userdesicion == True and is_nick_exist(self.username)==False:
                
                
                
                print('Are you sure about your name because its not exist please try again: ')
                self.username = self.taking_username()
                exit_question()
                
            
            
            if is_nick_exist(self.username) == True:
                '''log in here'''
                pass

            
    
        elif self.usersdesicion==False:
            self.username = self.taking_username()
            
        
        
        
        
        
        
        
        
        elif self.usersdesicion=='exit!1!':
            exit_question()
        
        
        
        '''WHEN ACCOUNT IS EXIST ACCORDINGLY USER'''
        if self.existance.lower() == 'y': #control and login part
            
            self.username = input('Whats your username')
            while not self.nick_exist():#when nick is not exist
                self.username = input('Whats your username..')
            
            
            '''WHEN ACCOUNT IS NOT EXIST ACCORDINGLY USER'''
        elif self.existance.lower()== 'n':#creating a new account   
            self.username = self.set_username()
        
            '''         exit time :(           '''
            
            if self.username == False: #player want to quit
                '''user want to go out !!'''
                
            
            else:

        ###desicion taking time y or n
        
        
        if isinstance(self.adresses,Address):
            if isinstance(self.wallet,Wallet):
                
                self.wallet.update_json(self.wallet.capital)
                
                ''' ++ self.adresses.update_json'''
                
                
                self.is_account_ready=True        
            else:
                self.is_account_ready=False
        else:
            self.is_account_ready = False
   
        
        
        
        
        