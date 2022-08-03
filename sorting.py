
def sorting(x):
    l=len(x)
    for i in range(l):
        for j in range((i+1),l):
            if x[i]>x[j]:
                l1=x[i]
                x[i]=x[j]
                x[j]=l1
    print(x)    




a = [95,45,-12,34,0,1,24,-32,54]
sorting(a)