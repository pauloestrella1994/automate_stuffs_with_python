def IsPhoneNumber(phone):
    '''
    Check if this is a brazillian valid phone number 
    Ex: (55)55555-5555
    '''

    if len(phone) != 14:
        raise Exception('wrong number exception 1')
    
    if phone[0] != '(' and phone[3] != ')':
        raise Exception('wrong number exception 2')
    
    for i in range (1, 2):
        if not phone[i].isdecimal():
            raise Exception('wrong number exception 3')
    
    for i in range (5, 9):
        if not phone[i].isdecimal():
            raise Exception('wrong number exception 4')
    
    if not phone[9] == '-':
        raise Exception('wrong number exception 5')
    
    for i in range (11, 14):
        if not phone[i].isdecimal():
            raise Exception('wrong number exception 6')
    
    return True

phone = input('text your phone to validate: ')
print(IsPhoneNumber(phone))
