import json
import os

class User:
    def __init__(self, username , password , email):
        self.username = username 
        self.password = password
        self.email = email
        

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        # Load users from .json file
        self.loadUser()

    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)


    def register(self , user:User):
        self.users.append(user)
        self.savetoFile()
        print("User created...")

    def login(self,username,password):
        
            for user in self.users:
                if user.username == username and user.password == password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print("Succesfully logged in...")
                    return 
                print("Login failed. Incorrect username or password")
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Succesfully logged out...")

    def identity(self):
        if self.isLoggedIn :
            print(f"username {self.currentUser.username}")
        else:
            print("Not logged in..")


    def savetoFile(self):
        liste = []
        for user in self.users:
            liste.append(json.dumps(user.__dict__))

        with open("users.json","w") as file :
            json.dump(liste,file)

repository = UserRepository()


while True :
    print("Menu".center(50,'*'))
    selection = input("1- Register\n2- Log in\n3- Log out\n4- Identity\n5- Exit\nSelected: ")
    if selection == '5':
        break
    else:
        if selection == '1':
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")

            user = User(username=username, password=password , email=email) 
            repository.register(user)

            print(repository.users)
        elif selection == '2':
           if repository.isLoggedIn:
              print("Already logged in..")
           else:
              username = input("Username : ")
              password = input("Password : ")

           repository.login(username,password)
        elif selection == '3':
            repository.logout()
        elif selection == '4':
            repository.identity()
        else:
            print("Invalid selection")

            

            
        