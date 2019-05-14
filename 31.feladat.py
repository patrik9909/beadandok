import re

def kukac(email):

    if re.search("[@.]", email) is None:
        return False
    else:
        return True

def hossz(email):
    if len(email) >= 12:
        return True
    else:
        return False
def vege(email):
    l=[]
    for i in email[-3:]:
        l.append(i)
    if "1"in l or "2" in l or "0" in l or "3" in l or "4" in l or "5" in l or "6" in l or "7" in l or "8" in l or "9" in l:
            return False
    else:
            return True

def ketpont(email):
    if (email.find("..") == -1):
        return True
    else:
        return False

email=1
while (email) !="0":
    email = input("add meg az email címed!")


    if kukac(email) is True and hossz(email) is True and ketpont(email) is True and vege(email) is True:
        continue
    print("rosz email formatum")