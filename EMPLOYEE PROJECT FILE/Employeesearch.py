import pickle
def searchemployee():
    with open("empdetails.data","rb") as fp:
        records=[]#create empty list to store records
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        res=False
        empn=int(input("\tEnter Employee Number To Search:"))
        for record in records:
            if record[0]==empn:
                res=True
                break
        print("-"*50)
        if res:
            print("\tEmployee Found And Valid.")
        else:
            print("\tEmployee Not Found And In-Valid.")
        print("-"*50)

