def swap_lines(file1, file2):
    with open(file1, 'r') as f1:
        lines1 = f1.readlines()

    with open(file2, 'r') as f2:
        lines2 = f2.readlines()

    middle_index = len(lines1) // 2

    lines1[middle_index], lines2[-1] = lines2[-1], lines1[middle_index]

    with open(file1, 'w') as f1:
        f1.writelines(lines1)

    with open(file2, 'w') as f2:
        f2.writelines(lines2)

file1 = 'WEEK7/file1.txt'
file2 = 'WEEK7/file2.txt'
swap_lines(file1, file2)

print("Lines swapped successfully.")
