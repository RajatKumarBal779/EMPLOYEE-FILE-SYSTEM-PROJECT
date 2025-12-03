import pickle
import sys
sys.path.append("D:\\ADVANCE  FUNCTION PYTHON(COACHING)\\8 custom Exceptions and raise keyword")
from nameexcept import ZeroNameLengthError,SpaceError,InvalidNameError
from namevalidation import validate
def uniqueemp(lst):
    with open("empdetails.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        found=True
        for record in records:
            if record[0]==lst[0]:
                found=False
        return found

def addemployee():
    while True:
        try:
            with open("empdetails.data","ab") as fp:
                lst=[]#create an empty list for adding employee values
                print("-"*50)
                empno=int(input("\tEnter Employee No:"))
                en=input("\tEnter Employee Name:")
                empname=validate(en)
                empsal=float(input("\tEnter Employee Salary:"))
                ec=input("\tEnter Employee Company Name:")
                empcomp=validate(ec)
                print("-"*50)
                #append emp values to list object
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                lst.append(empcomp)
                #save the iterable object content to the file
                if uniqueemp(lst):
                    pickle.dump(lst,fp)
                    print("\tEmployee Data Saved As Record In File Successfully.")
                else:
                    print("\tEmployee Number Already Exist--Try With Unique Employee Number.")
                print("-"*50)
                ch=input("\tDo You Want To Enter Another Employee Details (yes/no):")
                if ch.lower()=="no":
                    break
                print("-"*50)
        except ValueError:
            print("\tDon't Enter Alnums,Str And Symbol In Employee Number And Salary.")
        except ZeroNameLengthError:
            print("\tEnter Your Name/Company Name")
        except SpaceError:
            print("\tDon't Enter Space For Your Name/Company Name")
        except InvalidNameError:
            print("\tInvalid Name/Company Name--Try Again.")




