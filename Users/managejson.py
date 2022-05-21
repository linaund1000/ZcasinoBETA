'''smile , you are lucky'''
import json
def get_dictionary(target):
    'return all dictionary'
    f = open(f'jsondatas\\{target}.json','r')
    j = json.loads(f.read())
    f.close()
    return j

def save_dictionary(updated_dictionary,target):           
    f=open(f'jsondatas\\{target}','w')
    f.write(json.dumps(updated_dictionary))
    f.close()        
    