import re, PyPDF2

phoneRegex = re.compile(r'''
                            # some phones examples that we need to find
                            # 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
                        (
                            ((\d\d\d) | (\(\d\d\d\)))?    #area code
                            (\s|-)    #first separator
                            \d\d\d    #first 3 digits
                            -    #separator
                            \d\d\d\d    #last 4 digits
                            (((ext(\.)?\s)|x) #extension word-part (optional)
                                (\d{2,5}))?   #extension number-part (optional)
                        )
                        ''', re.VERBOSE)

emailRegex = re.compile(r'''
                        # some.+_thing@(\d{2, 5})?.com
                        [a-z0-9_.+]+   #name part
                        @    #@ symbol
                        [a-z0-9_.+]+   #domain name part

                        ''', re.VERBOSE | re.I)

pdfFile = open('regular_expressions/project/examplePhoneEmailDirectory.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
pages = reader.numPages

data = ''
for pageNum in range(pages):
    page = reader.getPage(pageNum)
    data += page.extractText()

subs = re.compile(r'[\n]')
clean_data = subs.sub("", data)

extracted_phone = phoneRegex.findall(clean_data)

all_phone_numbers = []
for phoneNumber in extracted_phone:
    all_phone_numbers.append(phoneNumber[0])

extracted_email = emailRegex.findall(clean_data)

print(extracted_email)