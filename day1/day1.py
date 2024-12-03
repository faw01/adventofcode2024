def parse_input(file_path):
    with open(file_path, "r") as file:
        pairs = []
        for line in file:
            line = line.strip()
            if line:
                numbers = line.split()
                if len(numbers) >= 2:
                    try:
                        pairs.append([int(numbers[0]), int(numbers[1])])
                    except ValueError:
                        continue

        list1, list2 = zip(*pairs) if pairs else ([], [])
        return list(list1), list(list2)


left, right = parse_input("input.txt")
# left = [3, 4, 2, 1, 3, 3]
# right = [4, 3, 5, 3, 9, 3]


# part one
def pair_logic(left, right):
    total_distance = 0

    while left and right:
        smallest_left = min(left)
        smallest_right = min(right)
        smallest_left_index = left.index(smallest_left)
        smallest_right_index = right.index(smallest_right)

        distance = calculate_distance_from_pair(smallest_left, smallest_right)
        total_distance += distance

        left.pop(smallest_left_index)
        right.pop(smallest_right_index)

    return total_distance


def pair(left, right):
    return pair_logic(left.copy(), right.copy())


def calculate_distance_from_pair(num1, num2):
    return abs(num1 - num2)


# puzzle answer
print(pair(left, right))


# part two
def convert_to_hashmap_frequency(list):
    return {item: list.count(item) for item in list}


def similarity(left, right):
    total = 0
    for num in left:
        frequency_in_right = right.count(num)
        total += num * frequency_in_right
    return total


# puzzle answer
print(similarity(left, right))
