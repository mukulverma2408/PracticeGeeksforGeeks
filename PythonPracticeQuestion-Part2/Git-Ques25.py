#Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

def PrintEmail(email):
    uname, domain = email.split("@")
    print(uname)
    print(domain)
    company = domain.split(".")[0]
    print(company)

PrintEmail("mukul.verma@fil.com")

