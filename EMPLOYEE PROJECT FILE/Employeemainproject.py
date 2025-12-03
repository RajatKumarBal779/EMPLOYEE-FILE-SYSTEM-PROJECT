from Empmenu import menu
from Employeeadd import addemployee
from Employeesearch import searchemployee
from Employeeview import viewallemp,viewemp
from Employeeupdate import updateemployee
from Employeedelete import deleteemployee
menu()
while True:
    try:
        ch=int(input("\tEnter Your Choice:"))
        match(ch):
            case 1:
                addemployee()
            case 2:
                deleteemployee()
            case 3:
                updateemployee()
            case 4:
                viewemp()
            case 5:
                viewallemp()
            case 6:
                searchemployee()
            case 7:
                print("\tThanks For Using This Project.")
                break
            case _:
                print("\tYour Choice Of Selection Is Wrong--Try Again.")
    except ValueError:
        print("\tDon't Enter Alnums,Str And Symbol for Choice--Try Again.")
