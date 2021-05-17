from datetime import date
import json
import requests

cachelist = {}

def cache1d(function):
    def wrapper(name): #defintion wrapper function
        if name not in cachelist: #if entry does not exist
            cachelist[name] = {"date": 0, "info": ""} #append to cachelist
        if cachelist[name]["date"] == date.today(): #if entry in cahcelist is from today
            print("already existed")
            return cachelist[name]["info"] #retrun cachelist-entry
        else:
            info = function(name) #get new data
            cachelist[name]["info"] = info #store new data in cachelist
            cachelist[name]["date"] = date.today() #store timestamp of entry
            print("new request")
            return info #return the new data
    return wrapper #return wrapper function
