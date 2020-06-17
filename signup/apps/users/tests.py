import json

source=[
    {"name":"my document","id":1 , "parentid": 0 },
    {"name":"photos","id":2 , "parentid": 1 },
    {"name":"Friend","id":3 , "parentid": 2 },
    {"name":"Wife","id":4 , "parentid": 2 },
    {"name":"Company","id":5 , "parentid": 2 },
    {"name":"Program Files","id":6 , "parentid": 1 },
    {"name":"intel","id":7 , "parentid": 6 },
    {"name":"java","id":8 , "parentid": 6 },
]

def getChildren(id=None):
    sz=[]
    for obj in source:
        if obj["parentid"] == id:
            sz.append({"id":obj["id"],"name":obj["name"],"children":getChildren(obj["id"])})
    return sz

print(json.dumps(getChildren(0)))




