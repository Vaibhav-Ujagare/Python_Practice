add=""
rem=""
result=""
# a="1010"
# b="1011"
a="1"
b="111"
if(len(a)>len(b)):
    b = ("0"*abs(len(a)-len(b)))+b
else:
    a = ("0"*abs(len(a)-len(b)))+a

for i in range(1,len(a)+1):
    i=i*-1
    if (a[i] == "1") and (b[i] == "1"):
        if rem == "1":
           add="1"
           result =add+result
        else:
           add="0"
           result = add+ result
           rem="1"
    elif (a[i] == "0") and (b[i] == "0"):
        if rem == "1":
            add = "1"
            result = add + result
            rem = "0"
        else:
            add = "0"
            result = add + result
    elif ((a[i] == "1") and (b[i] == "0")) or ((a[i] == "0") and (b[i] == "1")):
        if rem == "1":
            add = "0"
            result = add + result
            # rem = "0"
        else:
            add = "1"
            result = add + result
        
if(rem=="1"):
    result = "1"+result

print(result)