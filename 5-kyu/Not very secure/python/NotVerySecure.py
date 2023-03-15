def alphanumeric(password):
    if password!="":
        for x in password:
            if x.isnumeric() or x.isalpha():
                pass
            else:
                return False
    else:
        return False
    return True
