def find_three_numbers(arr, P):
    arr.sort()  # Сортуємо масив

    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == P:
                return True
            elif current_sum < P:
                left += 1
            else:
                right -= 1
    return False

# Приклад використання функції
arr = [1, 2, 3]
P = 6
print(find_three_numbers(arr, P))  # True йопта
