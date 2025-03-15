N = int(input())

if N < 1 or N > 15:
    print("Invalid N")
else:
    print((2**N+1)**2)