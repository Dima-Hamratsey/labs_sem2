def find_three_numbers(arr, P):
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        remaining_sum = P - arr[i]
        left, right = i + 1, n - 1
        while left < right:
            two_sum = arr[left] + arr[right]
            if two_sum == remaining_sum:
                return True
            elif two_sum < remaining_sum:
                left += 1
            elif two_sum  > remaining_sum:
                right -= 1
    return False

arr = [1, 2, 3]
P = 6
print(find_three_numbers(arr, P))  # True
