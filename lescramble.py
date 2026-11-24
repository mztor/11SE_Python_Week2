def scrambleIt(val, key):
    c = val[-key:] #grab the last x letters
    out = c + val[:len(val)-key] #grab c + the first len(letters)-key  
    
    return out


key = int(input("Key: "))
msg = input("")
messages= []
while msg != "":
    scram = scrambleIt(msg, key)
    print(scram)
    msg = input("")

