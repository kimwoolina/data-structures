# python3

def build_heap(data):
    swaps = []
    start = len(data) //2

    for i in range(start, -1, -1):
        sift_down(data, i, swaps)
        
    return swaps

def sift_down(data, i, swaps):
    size = len(data)
    l = left_child(i)
    r = right_child(i)
    min_index = i

    if l < size and data[l] < data[min_index]:  # Check if left child is within bounds
        min_index = l

    if r < size and data[r] < data[min_index]:  # Check if right child is within bounds
        min_index = r


    if i != min_index:
        swaps.append((i, min_index))
        temp = data[min_index]
        data[min_index] = data[i]
        data[i] = temp
        sift_down(data, min_index, swaps)


def left_child(i):
    left_child = 2*i +1
    return left_child


def right_child(i):
    right_child = 2*i + 2
    return right_child


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
