from ion import *

def keytogglebuild(keyname,value=0):
  return {"name":keyname,"value":value,"lastdown":0}

def keytoggle(key):
  # conditions of use:
  #  - inside a loop
  #  - key is a dictionary
  #  - key has at least 3 attributes:
  #    "name", "value" and "lastdown"
  
  if keydown(key["name"]) and not key["lastdown"]:
    key["value"]= (key["value"]+1)%2
    key["lastdown"]=(key["lastdown"]+1)%2
    return 1
  if not keydown(key["name"]):
    key["lastdown"]=0

def test():
  k_ok=keytogglebuild(KEY_OK)

  while 1:
    keytoggle(k_ok)
    print(k_ok["value"],k_ok["lastdown"])
# i think thats the most efficient way
# not sure tho

# make it so that we dont have to make key 
# objects
# basically automate a list of keys in a 
# keytoggle class
