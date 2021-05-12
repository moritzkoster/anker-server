from datetime import date

cachelist = {}

#last = {"anker": {"date": 0, "info": ""}}

def cache1d(function):
    def wrapper(name):
        if name not in cachelist:
            cachelist[name] = {"date": 0, "info": ""}
        if cachelist[name]["date"] == date.today():
            print("already existed")
            return cachelist[name]["info"]
        else:
            info = function(name)
            #info = "this strange shit"
            cachelist[name]["info"] = info
            cachelist[name]["date"] = date.today()
            print("new request")
            return info
    return wrapper

#
# def cachelist():
#     cachelist = {}
#     for element in list:
#         cachelist[element] = {"date": 0, "info": ""}
#     return cachelist

#cachelist = cachelist()
