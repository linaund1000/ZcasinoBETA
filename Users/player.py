
"""
creation of user:

    Player class set the wallet and adresses object if objects are ready player objects attributes are saved in json 

users:[]
      
    """
from Users.wallet import Wallet
from Users.addresses import Address


class Player:
    """i have no idea about what i am doing"""
    
    
    def __init__(self,username):

        self.username = username
        
        self.wallet = Wallet(username)
        
        self.adress = Address(username)
        
                
        

