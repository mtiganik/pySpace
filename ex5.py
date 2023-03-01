f = open("input.txt")

data =""
for x in f:
    data = data + x

def sort_file(inp, insep = ",", inend = "\n", outsep="in", outend="in"):
    arr = inp.split("\n")
    
    #[x for x in arr if x ]
    while '' in arr:
        arr.remove('')
    arr = [x for x in arr if not x.startswith("#")]
    change = True
    while change == True:
        change = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                change = True
    listToStr = '\n'.join([str(elem) for elem in arr])
    if outsep != "in":
        listToStr= listToStr.replace(",",outsep)
    if outend != "in":
        listToStr= listToStr.replace("\n", outend)
    return listToStr

print(sort_file(data))
print("######")
print(sort_file('b\ny\na'))
print("######")
print(sort_file('b,b\ny,y\na,a', outsep=':', outend='\t'))
print("######")
print(sort_file('b,q\n\n#p,y\na,o', outsep='-'))
print("######")
print(sort_file('2,3,d\n2,4,x\n2,4,a\n\n\n', outend=' -- end\n'))