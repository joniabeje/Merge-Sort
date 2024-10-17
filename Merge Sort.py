# 1)

Grades = {'Charles': 100, 'Chris': 85, 'Ema': 60, 'Ariel': 65, 'John': 85, 'Patrick': 55, 'Stella': 50, 'Sharon': 89,
          'Victoria': 83, 'Debby': 90, 'Suzanne': 78, 'Kevin': 76}


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][1] <= right[right_index][1]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


sorted_grades = merge_sort(list(Grades.items()))

for name, grade in sorted_grades:
    print(f"{name}: {grade}")

print("-----------------")

# 2) Just changing the sign for sorting in descending order

Grades = {'Charles': 100, 'Chris': 85, 'Ema': 60, 'Ariel': 65, 'John': 85, 'Patrick': 55, 'Stella': 50, 'Sharon': 89,
          'Victoria': 83, 'Debby': 90, 'Suzanne': 78, 'Kevin': 76}

def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        # Changed comparison to > for descending order
        if left[left_index][1] > right[right_index][1]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

sorted_grades = merge_sort(list(Grades.items()))

for name, grade in sorted_grades:
    print(f"{name}: {grade}")


print("-----------------")

# 3) Adding alphabetical sorting for students with identical grades when ascending

Grades = {'Charles': 100, 'Chris': 85, 'Ema': 60, 'Ariel': 65, 'John': 85, 'Patrick': 55, 'Stella': 50, 'Sharon': 89,
          'Victoria': 83, 'Debby': 90, 'Suzanne': 78, 'Kevin': 76}


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        left_name, left_grade = left[left_index]
        right_name, right_grade = right[right_index]

        if left_grade < right_grade or (left_grade == right_grade and left_name < right_name):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

sorted_grades = merge_sort(list(Grades.items()))

for name, grade in sorted_grades:
    print(f"{name}: {grade}")