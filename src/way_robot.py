field = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]


def reverse_l1(arr):
    return arr[::-1]


def find_way_robot(arr):
    robot_way = []
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        if i % 2 == 0:
            robot_way.extend(arr[i])
        else:
            reversed_list = reverse_l1(arr[i])
            robot_way.extend(reversed_list)
    return robot_way


print(find_way_robot(field))





field = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]


def find_way_robot(arr):
    list_2 = []
    way_robot = []
    strings = len(arr)
    columns = len(arr[0])
    for i in range(columns):
        for j in range(strings):
            list_2.append(arr[j][i])
        if i % 2 == 0:
            list_2.reverse()
        way_robot.extend(list_2)
        list_2 = []

    return way_robot


print(find_way_robot(field))
