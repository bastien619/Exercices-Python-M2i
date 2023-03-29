

def hanoi(n,A,B,C) :
    if n>1 :
        hanoi(n-1,A,C,B)
        hanoi(1,A,B,C)
        hanoi(n-1,B,A,C)
    else :
        C.append(A.pop())
        print("A : {}\nB : {}\nC : {}\n".format(A,B,C))

def init(N) :
    A,B,C = [i for i in reversed(range(1,N+1))],[],[]
    hanoi(N,A,B,C)