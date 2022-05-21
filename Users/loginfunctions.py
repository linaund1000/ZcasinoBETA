def exit_question():
    i = input('enter q here if you want to quit : ')
    if i == 'q':
        return sys.exit()
    else:
        pass
def have_u_got_account():
        i = input('have you got account? (y or n) :')
        while i not in ['y','n']:
            print('your input is invalid please try again or exit with e')
            i = ('have you got account? (y or n) :')
            if i =='e':
                return 'exit!1!'
        if i == 'y':
            return True
        else:
            return False
def taking_username():
    
    '''just taking name and test its characters'''
    def is_verified_input(username):
        try:
            username = str(username)   
            if username.isalpha():
                if len(username)<15 and len(username)>4:
                    return True
            
        except:
            return False    
            
    username =''
        
    while is_verified_input(username)== False:
        username=input('Choose a username : ')
        return username
def set_username(self):
        '''returns self.username imidiately quit '''
        username_ready = False
        while username_ready == False:
            
            
            username=input('Choose a username : ')
            if username.isalpha() == True: 
                
                if 4< len(username) < 15:
                    if self.nick_exist() == True:
                        print('account is already exist')
                        print('to choose another username -> n')
                        print('quit --> q ')
                        desicion = input('enter a desicion : ')
                        
                        while desicion.lower() not in ['n','q']:
                            print('You just entered invalid character, please be carefull!')
                            desicion = input('enter another desicion : ')
                        if desicion == 'q':
                            sys.exit()
                        elif desicion =='n':
                            username_ready == False
                    else:
                        username_ready == True
                        break
                               
                else:
                    print('username length can not have more than 15characters and less than 4 characters')
                    username_ready = False 
            
            else:
                print('username can not have any symbol just alphabetical characters...')
        
        username_ready = True
        return username
def is_nick_exist(username):
        '''verified nick in usernames.json data'''
        f = open(r'jsondatas\usernames.json','r')
        j= json.loads(f.read())  
        f.close()  
        if username in j['nicks']:
                return True
        else:
            return False
def save_nick(self):
    
    '''save the nick in json data which is usernames.json'''
        
        
    f = open(r'jsondatas\usernames.json','r')
    j  =  json.loads(f.read())
    f.close()
         
    if self.username not in j['nicks']:
        if self.username != None:
            j['nicks'].append(self.username)
        else:
            raise ValueError
        
        fl = open(r'jsondatas\usernames.json','w')
        fl.write(json.dumps(j))
        fl.close()