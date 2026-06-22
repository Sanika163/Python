#Difference between List and Tuple

#               List        Tuple
#Ordered        Yes         Yes
#Indexed        Yes         Yes
#Mutable        Yes         No
#Heterogeneous  Yes         Yes

def main():
    DataList = [10, 88.43, True, "Pune"]
    DataTuple = (10, 88.43, True, "Pune")

    print(DataList)
    print(DataTuple)

    print(DataList[0])
    print(DataTuple[3])
    
    DataList[1] = 11
    #DataTuple[1] = 11  #Error : Cannot change tuple

    print(DataList[1])

if(__name__ == "__main__"):
    main()