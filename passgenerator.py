print('''
(program start)

- Contains 8-16 characters
- Contains one of the special characters: %$#^&*!@()
- Contains at least one number 0-9
- Contains at least one capital letter
- Starts with a lowercase letter
- Does not contain the phrase “pass” in any format
- Does not contain the phrase “qwerty” in any format
- Does not contain the phrase “123”      

Please enter a password that conforms to the above restrictions:      
''')


Is_Valid = False
special_characters = "%$#^&*!@()"
numerical_values = "0123456789"

def validate_password(password):
    
    if(len(password) < 8 or len(password) > 16):
        print("This password does not meet the following requirements:")
        print("Contains 8-16 characters")
        return False
    if(not set(password).intersection(special_characters)):
        print("This password does not meet the following requirements:")
        print("Contains one of the special characters: %$#^&*!@()")
        return False
    if(not set(password).intersection(numerical_values)):
        print("This password does not meet the following requirements:")
        print("Contains at least one number 0-9")
        return False
    if(not any(char.isupper()for char in password)):
        print("This password does not meet the following requirements:")
        print("Contains at least one capital letter")
        return False
    if(not (password[0].islower())):
        print("This password does not meet the following requirements:")
        print("Starts with a lowercase letter")
        return False 
    if ("pass" in password):
        print("This password does not meet the following requirements:")
        print("Does not contain the phrase “pass” in any format")
        return False
    if("qwerty" in password):
        print("This password does not meet the following requirements:")
        print("Does not contain the phrase “qwerty” in any format")
        return False
    if("123" in password):
        print("This password does not meet the following requirements:")
        print('Does not contain the phrase “123”')
        return False   
    return True


while(not Is_Valid):
    password=input()
    Is_Valid = validate_password(password)
    if (Is_Valid):
        print("Success!")
        break
    