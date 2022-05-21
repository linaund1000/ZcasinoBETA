import json
import managejson

class Address:
    '''
        =>save adress in adresses.json
        --==>save_dictionary function()
        =>create adress 
        =>delete adress
        =>update adress
        =>read adress
        ===>test_mail = show whether input is mail or not
        ===>test_phone = show whether input is phone number or not
        ====>is_exist_phone&mail
        
        
        
        
        note : 
            doesnt test the username that were given 
            thats in responsibility of login module
        '''
    
    def __init__(self,username):
        '''self.adresses = all adresses
            self.adresses[self.username] = users data'''
        self.username = username
        if ' ' in username:
            raise ValueError('username can not have any space')
        
        self.adresses  = managejson.get_dictionary('adresses')
        
        if not self.username in self.adresses:    
            self.setting_first_time()

    

    def delete_adress(self,adress_type):
        '''adress type can be 'mail' or 'number' nothing else'''
        
        list_of_adress =self.adresses[self.username][adress_type]
        count=0
        for i in list_of_adress:
            print(count,'. ',i)
            count = count +1
        delete_num=False
        while  delete_num==False:
            try:    
                delete_num = int(input('enter a index of adress you want to delete : '))
                if delete_num > count:
                    raise ValueError
                elif delete_num < 0:
                    raise ValueError
            except:
                print('your entry is not correct please enter a entry exist on the list')    
            
            
            if delete_num < len(list_of_adress):
                if delete_num >= 0:
                    
                    print('you removed')
                    
                    self.adresses[self.username][adress_type].pop(delete_num)
                    
                    managejson.save_dictionary(self.adresses,'adresses')#saved
                    break
            delete_num = False
    
    def get_main_adress(self,adress_type):
        '''adress type can be 'mail' or 'number' nothing else'''
        try:
            main_mail = self.adresses[self.username][adress_type][0]
            return main_mail
        except IndexError:
            print('you have no verificated',adress_type)
       
       
       
        
    def upload_new_mail_adress(self,new_adress):
        
        if  new_adress not in self.adresses[self.username]['mail']:
            self.adresses[self.username]['mail'].append(new_adress)        
            managejson.save_dictionary(self.adresses,'adresses')
            
            
        while new_adress in self.adresses[self.username]['mail']:
            new_adress = input('this mail adress already exist enter another one or q for quit : ')
            if new_adress in ['q','Q']:
                break
            elif new_adress.lower() != 'q':
                self.get_all_mails_of_user().append(new_adress)
                managejson.save_dictionary(self.adresses,'adresses')
                break
    def upload_new_phone_adress(self,new_adress):
        d = managejson.get_dictionary('adresses')
        d[self.name]['phone'].append(new_adress)
        managejson.save_dictionary(d,'adresses')
    
    
    
    
    
    def get_all_mails_of_user(self):
        return self.adresses[self.username]['mail']
    def get_all_phones_of_user(self):
        return self.adresses[self.username]['phone']
    
    
    def phone_input():#not ready
        '''taking phone question it return phone number'''
        p = input('your phone number :')
        
        '''phonenumber_verification(p)'''
        return p
    def mail_input():#not ready
        
        '''taking phone question it return mailadress'''
        m= input('your mail adress :')
        
        '''mail_verification(p)'''
        return m
    
    def setting_first_time(self):
        self.adresses[self.username]  = {'mail':[],'phone':[]}
        managejson.save_dictionary(self.adresses,'adresses')
if __name__ == '__main__':
    username  = 'bromance.com'
    a = Address(username)
    print(a.get_main_adress('mail'))
    a.upload_new_mail_adress('seni_gidi_topal.com')
    print(a.get_main_adress('mail'),'main adress is that')
    a.delete_adress('mail')

    