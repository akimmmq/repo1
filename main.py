def setList():
    n = int(input('Amount of elements: '))
    ilist = []
    for i in range (n):
        ilist.append(int(input(f'Enter the number ({n} times): ')))
    
    return ilist

def getMax(ilist):
    print('Max element: ' , max(ilist))
