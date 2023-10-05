import re
import os

def checkLength(pwd):
    if len(pwd)<=8:
        return False
    return True

# check if symbols, capital
def checkCharacters(pwd):
    if not any(char.isupper() for char in pwd):
        return False 
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]',pwd):
        return False
    if not any(char.isdigit() for char in pwd):
        return False
    return True

def checkCommonPasswords(pwd):
    commonPwdList = os.listdir("./Lists")
    for pwdListFile in commonPwdList:
        with open(f'./Lists/{pwdListFile}',"r",encoding="utf-8") as pwdList:
            for commonPwd in pwdList:
                if(commonPwd.rstrip("\n") == pwd):
                    return False 
    return True