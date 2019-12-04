import bisect


def my_hamming(n):
    """Returns the nth hamming number"""

    BASES = [2, 3, 5]
    hamming_nums = [1]
    for use_idx in range(n):
        use_num = hamming_nums[use_idx]
        for base in BASES:
            num = base * use_num
            if num not in hamming_nums:
                bisect.insort_left(hamming_nums, num)

    return hamming_nums[n-1]


def hamming1(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        print(f'hamms={hamms}, expos={expos}, next_hamms={next_hamms}')
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]

def hamming2(n):
    bag = {1}
    for _ in range(n - 1):
        head = min(bag)
        bag.remove(head)
        bag |= {head*2, head*3, head*5}
    return min(bag)

import time

start = time.time()
# print(my_hamming(5000))
print(hamming1(10))
# print(hamming2(5000))
# for i in range(1, 20):
#     print(hamming1(i))

print(f'it take {time.time() - start} sec')
