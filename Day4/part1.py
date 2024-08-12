with open("./Day4/input.txt") as f:
    data = f.readlines()


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
for line in data:
    card_values = line.split(":")[1]
    card_values = card_values.split("|")
    winner_cards = card_values[0].split()
    have_cards = card_values[1].split()
    cnt = 0
    sorted_have_cards = sorted(have_cards)
    for i in winner_cards:
        if binary_search(sorted_have_cards, i):
            cnt += 1
    if cnt != 0:
        res += pow(2, cnt - 1)

print(res)
