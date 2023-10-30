def count():
    count = 0
    f=open("report.txt","r")
    for i in f.readlines():
        if i[0] in ["m",'i','I',"M"]:
            count=count+1
    return count
print("The total number of lines starting with I and M are::: ",count())
