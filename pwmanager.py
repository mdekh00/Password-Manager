class BasePasswordManager:
    old_passwords=[]
    
#Gets the current Password
    def get_password(self):
        return self.old_passwords[-1]
    
#Checks if the entered password matches
    def is_correct(self, password):
        return self.old_passwords[-1] == password
    
class PasswordManager(BasePasswordManager):
    
# set new password
    def set_password(self, password):
        if(len(password)<=6):
            print("Password should be greater than 6 characters\n")
        else:
            if(len(self.old_passwords)==0):
                self.old_passwords.append(password)
                print("Password created\n")
            else:
                new_level = self.get_level(password)
                old_level = self.get_level()
                if (new_level>=old_level):
                    self.old_passwords.append(password)
                    print("Password changed\n")
                else:
                    print("password level needs to increased\n")
                
#Gets the level of the password 
    def get_level(self, data = " "):
        if(data.isalpha() or data.isnumeric() or data.strip()==""):
            level = "Easy" 
        elif(data.isalnum()):
            level = "Medium"
        else:
            level = "Difficult"
        return level
    
# End user menu starts here
ch = 1
while(ch!=4):
    print("1. Set Password")
    print("2. Check Password")
    print("3. Get Level of Password")
    print("4. Quit")
    ch = int(input("Enter your choice: "))

    pm = PasswordManager()
    old_passwords = pm.old_passwords
    if (ch==1):
        password= input("Enter Password: ")
        pm.set_password(password)
    elif(ch==2):
        print("Your Password is", old_passwords[-1], "\n")
    elif(ch==3):
        password = input("Enter password: ")
        print('Your Password Level is', pm.get_level(password), "\n")
    else:
        pass