def validate_pin(pin):
    if (len(pin)==4 or len(pin)==6):
        i=0
        c=0
        while i<len(pin):
            if pin[i].isdigit():
                c+=1
            i+=1
        if c==4 or c==6:
            return True
        else: 
            return False
    return False
            
print(validate_pin("1a3456"))
print(validate_pin("123456"))
print(validate_pin("-13456"))
print(validate_pin("134.56"))