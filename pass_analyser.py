import re

def analyzer(password):
    score=0
    remarks=[]
    c_pass=['Password@123','password123','welcome1234','P@sswORd','O1234$b']

    if len(password)>=8:
        score+=1
    else:
        remarks.append('A strong password must atleast contain 8 characters')
        

    if re.search(r'[A-Z]',password):
        score+=1
    else:
        remarks.append('A strong password must atleast contain 1 capital letter')
        

    if re.search(r'[a-z]',password):
        score+=1
    else:
        remarks.append('A strong password must contain a small letter')
        

    if re.search(r'[0-9]',password):
        score+=3
    else:
        remarks.append('A strong password must atleast contain a number')
        

    if re.search(r'[^\w\s]',password):
        score+=4
    else:
        remarks.append('A strong password must atleast contain a special character')
        

    if password in c_pass:
        remarks.append('Avoid common passwords like password@123, P@ssw0Rd')

    if score<=3:
        strength='Weak'
    elif score>3 and score<=6:
        strength='Moderate'
    else:
        strength='Very strong'

    return strength,remarks

user_password=input('Enter a password to analyze the strength: ')
strength,feedback=analyzer(user_password)


print(f'Password strength: {strength}')
if feedback:
    print("\nSuggestions for a strong password\n")
    for i in feedback:
        print(i)
        

#Suggestions for the user to how to create a strong password
print("\nSecure Password Practices:")
print(" - Use at least 12 characters.")
print(" - Mix uppercase, lowercase, numbers, and special characters.")
print(" - Avoid dictionary words and personal info.")
print(" - Don’t reuse passwords across sites.")
print(" - Use a password manager for strong, unique passwords.")

#Examples of strong password to the user
print("\n💡 Example Strong Passwords:")
print(" - C0mp!ex#Pass_92")
print(" - Tr!p7eL@yer#Sec")






        
