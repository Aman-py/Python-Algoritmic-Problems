L = int(input())
N = int(input())
for i in range(N):
    W,H = [int(temp) for temp in input().strip().split(' ')]
    if W< L or H< L:
        print("UPLOAD ANOTHER")
    elif (W and H) >= L:
        if W==H:
            print("ACCEPTED")
        else:
            print("CROP IT")
