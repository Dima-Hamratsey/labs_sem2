def read_file(file_path):
    with open(file_path, 'r') as file:
        try:
            columns, lines = map(int, file.readline().split())
        except ValueError:
            return 0

        matrix = []
        dict_of_letters = dict()

        for cur_line, line in enumerate(file):
            line = line.strip()
            temp_line = []

            for cur_column, char in enumerate(line):
                temp_line.append(char)

                if char in dict_of_letters:
                    dict_of_letters[char].append((cur_line, cur_column))
                else:
                    dict_of_letters[char] = [(cur_line, cur_column)]

            matrix.append(temp_line)

        return matrix, dict_of_letters, lines, columns


def get_answer(matrix, dict_of_letters, lines, columns):
    letters_on_path = {(0, columns - 1): [], (lines - 1, columns - 1): []}

    for column in range(columns - 2, -1, -1):
        for row in range(lines):
            was_in_neighbour = False

            for neighbour in dict_of_letters[matrix[row][column]]:
                if neighbour in letters_on_path and neighbour[1] > column:
                    letters_on_path[neighbour].append((row, column))
                    letters_on_path[(row, column)] = []

                if neighbour == (row, column + 1):
                    was_in_neighbour = True

            if was_in_neighbour or (row, column + 1) not in letters_on_path:
                continue

            letters_on_path[(row, column + 1)].append((row, column))
            letters_on_path[(row, column)] = []

    return letters_on_path


def get_paths(dict_of_paths, lines, columns):
    stack = [(0, columns - 1)]

    if lines - 1 != 0:
        stack.append((lines - 1, columns - 1))

    result = 0

    while stack:
        current_row, current_column = stack.pop()

        if current_column == 0:
            result += 1
            continue

        for neighbour in dict_of_paths[(current_row, current_column)]:
            stack.append(neighbour)

    return result


def write_result(output_file, result):
    with open(output_file, 'w') as file:
        file.write(str(result))


def ijones(input_file, output_file):
    ijones_matrix, letters_dict, lines, cols = read_file(input_file)
    dict_ijones = get_answer(ijones_matrix, letters_dict, lines, cols)
    result = get_paths(dict_ijones, lines, cols)
    write_result(output_file, result)
