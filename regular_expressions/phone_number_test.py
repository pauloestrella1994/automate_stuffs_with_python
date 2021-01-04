def IsPhoneNumber(phone):
    '''
    Check if this is a brazillian valid phone number 
    Ex: (55)55555-5555
    '''

    if len(phone) != 14:
        return False
    
    if phone[0] != '(' and phone[3] != ')':
        return False
    
    for i in range (1, 2):
        if not phone[i].isdecimal():
            return False
    
    for i in range (5, 9):
        if not phone[i].isdecimal():
            return False
    
    if not phone[9] == '-':
        return False
    
    for i in range (11, 14):
        if not phone[i].isdecimal():
            return False
    return True

message = 'Preciso que você me ligue amanhã em um desses números: (55)55555-5555 ou (55)44444-4444. É urgente!'

foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+14]
    if IsPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any number!')