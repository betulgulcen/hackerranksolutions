 #create a function
def check(a,L):
    if a=="pop":
        L.pop()
    if a=="print":
        print(L)
    if a=="reverse":
        L.reverse()
    if a=="sort":
        L.sort()
    return L

if __name__ == '__main__':
    N = int(input())
    main=[]
    L=[]
    for x in range (N):
        main.append([])
        main[x].extend(input().split())
        y=main[x][0]
        L=check(y,L)
        if y=="insert":
            L.insert(int(main[x][1]),int(main[x][2]))
        if y=="remove":
            L.remove(int(main[x][1]))
        if y=="append":
            L.append(int(main[x][1]))
