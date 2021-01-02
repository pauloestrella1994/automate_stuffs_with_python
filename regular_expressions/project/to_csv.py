from phone_and_email import extracted_email, all_phone_numbers

with open('email_phone.csv', 'w') as file:
    file.write('Email, Phone\n')
    for email, phone in zip(extracted_email, all_phone_numbers):
        file.write(email + ',' + phone + '\n')

    