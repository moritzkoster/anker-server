from datetime import date
import json
import requests

cachelist = {"coop": {},
            "denner": {},
            "spar": {},
            "migros" : {}
}

def cache1d(store): #decorator-Factory
    def decorator(function): #actual decorator
        def wrapper(name): #defintion wrapper function
            if name not in cachelist[store]: #if entry does not exist
                cachelist[store][name] = {"date": 0, "info": ""} #append to cachelist
            if cachelist[store][name]["date"] == date.today(): #if entry in cahcelist is from today
                print("already existed")
                return cachelist[store][name]["info"] #retrun cachelist-entry
            else:
                info = function(name) #get new data
                cachelist[store][name]["info"] = info #store new data in cachelist
                cachelist[store][name]["date"] = date.today() #store timestamp of entry
                print("new request")
                return info #return the new data
        return wrapper
    return decorator #return wrapper function
