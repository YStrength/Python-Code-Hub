T,K = map(int,input().split())
for i in range(K):
    n1,b,t,n2 = map(int,input().split())
    if t <= T:
        if b == 0:
            if n2 < n1:
                T += t
                print("Win %d!  Total = %d."%(t,T))
            else:
                T -= t
                print("Lose %d.  Total = %d."%(t,T))
                if T == 0:
                    print("Game Over.")
                    exit()
        if b == 1:
            if n2 > n1:
                T += t
                print("Win %d!  Total = %d." % (t, T))
            else:
                T -= t
                print("Lose %d.  Total = %d." % (t, T))
                if T == 0:
                    print("Game Over.")
                    exit()
    else:
        print("Not enough tokens.  Total = %d."%(T))