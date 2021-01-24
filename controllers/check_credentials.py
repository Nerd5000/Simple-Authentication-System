import re


class CheckCredentials:

    @staticmethod
    def checkmail(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, email.lower())):
            return True
        else:
            return False
