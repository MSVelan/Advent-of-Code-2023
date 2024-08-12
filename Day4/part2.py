with open("./Day4/input.txt") as f:
    data = f.readlines()

n = len(data)

mp = {}
for i in range(1, n + 1):
    mp[i] = 1


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


res = 0
for i in range(len(data)):
    card_values = data[i].split(":")[1]
    card_values = card_values.split("|")
    winner_cards = card_values[0].split()
    have_cards = card_values[1].split()
    cnt = 0
    sorted_have_cards = sorted(have_cards)
    for j in winner_cards:
        if binary_search(sorted_have_cards, j):
            cnt += 1
    if i + cnt + 1 <= n:
        res += mp[i + 1]  # Here, i is having zero based indexing
        for j in range(1, cnt + 1):
            mp[i + j + 1] += mp[i + 1]
    else:
        res += mp[i + 1]
        for j in range(1, n - i + 1):
            mp[i + j + 1] += mp[i + 1]

print(res)
