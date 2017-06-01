def Sort(list):
    size = len(list)
    for i in xrange(0,size-1):
        for j in xrange(i+1,size):
            #print list[i], list[j]
            if list[i] > list[j]:
                t = list[i]
                list[i] = list[j]
                list[j] = t

list = [ 5,1,4,2,3]
Sort(list)
print list