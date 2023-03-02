def sort_file(inp,*, insep = ",", inend = "\n", outsep=",", outend="\n"):
    arr = inp.split("\n")

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

try:
    sort_file('abc', "test") # -> TypeError
    raise Exception("2 positional arguments not allowed")

except TypeError: pass

# Example result
assert sort_file("2,3,d\n1,4,d\n8,2,z\n2,4,x\n2,4,a") == "1,4,d\n2,3,d\n2,4,a\n2,4,x\n8,2,z"

# A string with only one item per row
assert sort_file('b\ny\na') == 'a\nb\ny'

# Providing some keyword arguments
assert sort_file('b,b\ny,y\na,a', outsep=':', outend='\t') == 'a:a\tb:b\ty:y'

# Blank lines and lines starting with '#' should not appear in the result
assert sort_file('b,q\n\n#p,y\na,o', outsep='-') == 'a-o\nb-q'

# Proper sorting and ignore blank lines at the end
assert sort_file('2,3,d\n2,4,x\n2,4,a\n\n\n', outend=' -- end\n') == '2,3,d -- end\n2,4,a -- end\n2,4,x'

print("End of program")
print(sort_file('b,q\n\n#p,y\na,o', outsep='-'))