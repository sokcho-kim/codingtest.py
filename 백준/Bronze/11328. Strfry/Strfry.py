for i in range(int(input())):
    str1,str2 = map(sorted,list(input().split()))
    print(['Impossible','Possible'][str1==str2])