def login(Dashbroad):
    def Decorator(user):
        if user == "admin":
            print("Admin Login Successful")
            Dashbroad(user)
        else:
            print("Access Denied")
    return Decorator

@login
def Dashbroad(user):
    print("welcome to the dashboard")

Dashbroad("admin")
Dashbroad("other")