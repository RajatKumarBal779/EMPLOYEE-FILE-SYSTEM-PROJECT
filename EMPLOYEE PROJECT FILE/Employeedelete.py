import pickle
def deleteemployee():
    with open ("empdetails.data" ,"rb") as rp:
        records=[]
        while True:
            try:
                record=pickle.load(rp)
                records.append(record)
            except EOFError:
                break
        eno=int(input("\tEnter Employee Number For Delete The Record:"))
        res=False
        for index in range(len(records)):
            if records[index][0]==eno:
                res=True
                recindex=index
                break
        print("-"*50)
        if res:
            records.pop(recindex)
            #Place The Records from Main Memory To The File Of Secondary Memory
            with open("empdetails.data","wb") as wp:
                for record in records:
                    pickle.dump(record,wp)
                print("\tEmployee Records Deleted Successfully.")
        else:
            print("\tEmployee Details Doesn't Exist.")
        print("-"*50)