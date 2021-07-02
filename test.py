
def search_even(num):
    numlist=[]
    for i in range(1, num+1):
        if i %2==0:
            numlist.append(i)

    return numlist

number=50
print(search_even(number))