arr = []
for i in range(6):
    a = int(input())
    arr.append(a)

target = int(input())

def PairFound(x: int, y:int ):
    if((x+y) == target):
        print(f"Pair Found({x}, {y})")
        return

for i in range(6):
    for j in range(i+1, 6):
        PairFound(arr[i], arr[j])
        