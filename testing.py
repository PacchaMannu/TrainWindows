def func(a,*b,**c):
    print("a=",a)
    print("b=")
    print(b)
    print(c)
    for dd in b:
        print(dd)
    print("c=")
    for cc in c:
        print(cc)

func("this is a",
    "this should be b", 
    "this also should be b", 
    "b again", 
    c1="helo", 
    c2="my name", 
    c3="is dev")