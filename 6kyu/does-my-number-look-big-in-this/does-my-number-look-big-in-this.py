def narcissistic( value ):
    total = 0
    for x in str(value):
        total = int(x)**(len(str(value))) + int(total)
    if total == value or (len(str(value)) == 1):
        return True 
    else:
        return False
        
