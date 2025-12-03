import pickle
def updateemployee():
    with open ("empdetails.data","rb") as rp:
        records=[]
        while True:
            try:
                record=pickle.load(rp)
                records.append(record)
            except EOFError:
                break
        empno=int(input("\tEnter Employee Number To Update Salary And Company Name:"))
        res=False
        for index in range (len(records)):
            if records[index][0]==empno:
                recindex=index
                res=True
                break
        print("-"*50)
        if res:
            empsal=float(input("\tEnter Employee New Salary:"))
            empcomp=input("\tEnter Employee Company Name:")
            records[recindex][2]=empsal
            records[recindex][3]=empcomp
            #Place The Records Of Main Memory Into Secondary Memory.
            with open("empdetails.data","wb") as wp:
                for record in records:
                    pickle.dump(record,wp)
            print("\tEmployee Details Updated Successfully.")
        else:
            print("\tEmployee Details Not Found.")
        print("-"*50)


