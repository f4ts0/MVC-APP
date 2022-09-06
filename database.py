 ##ovo je model
 
class Database:
    def __init__(self, path):
        

        ''' 
         #ovo je inicijalno kad sam podatke pisao direkt u kod.
         # Mnogo je pametnije podatke drzati sa strane (u fajlu) pa usrkati u bazu
         self.data = {
             "IGOR": {"paid": 60, "due": 100},
             "JELENA": {"paid": 10, "due": 5},
             "PETAR": {"paid": 0, "due": 100},
             "MILICA": {"paid": 20, "due": 450}
         }
        '''
        with open(path, "r") as handle:
            #import json
            #self.data = json.load(handle)
            
            import yaml
            self.data = yaml.safe_load(handle)

            #import xmltodict
            #self.data=xmltodict.parse(handle.read()) ["root"]
            #print (self.data)

    def balance(self, acct_id):
        acct = self.data.get(acct_id)
        if acct:
            return int(acct["due"]) - int(acct["paid"])
        return None


    
    

     
