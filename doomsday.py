def solution(xs):
    if len(xs)<1 or len(xs)>50 or not(isinstance(xs,list)):
        return "0"
    if len(xs)==1:
        return str(xs[0])
    l = []
    for i in xs:
        if not(isinstance(i,int)) or abs(i)>1000:
            exit()
        else :
            l.append(abs(i))
    for i in l:
        if i==0 :
            l.remove(i)
    l.sort(reverse=True)
    if len(l)<=3 :
        if 1 in l:
            l1=[l[i] for i in range(len(l))]
    else:
        l1=[l[i] for i in range(len(l)-1)]
    p=1
    for i in l1:
        p*=i
    return str(p)
a = solution([2,0,2,2,0])
print(a)
