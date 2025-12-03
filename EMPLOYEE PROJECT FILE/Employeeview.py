import pickle
def viewemp():
    with open('empdetails.data', 'rb') as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        empno=int(input("\tEnter employee no:"))
        res=False
        for record in records:
            if record[0]==empno:
                res=True
                break
        print("-" * 50)
        if res:
            print("\tEmployee Number:{}".format(record[0]))
            print("\tEmployee Name:{}".format(record[1]))
            print("\tEmployee Salary:{}".format(record[2]))
            print("\tEmployee Company Name:{}".format(record[3]))
        else:
            print("\t{} Employee Number Not Found.".format(empno))
        print("-" * 50)

def viewallemp():
    with open("empdetails.data","rb") as rp:
        print("-" * 50)
        print("\tNUMBER\tNAME\tSALARY\tCOMPNAME")
        print("-" * 50)
        while True:
            try:
                record=pickle.load(rp)#will upload first list to record
                for val in record:#then iterate each value one by one in record
                    print("\t{}".format(val),end=" ")
                print()
            except EOFError:
                break




