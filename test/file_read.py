# using context manager

with open('file.txt', 'r') as f:
    size_to_read = 100
    # f.read(n) ==> n is the no of characters u want to read
    f_content = f.read(size_to_read)
    # f.tell() tells the position of the character of the file
    # print(f.tell())
    # print(f_content, end='')
    while len(f_content) > 0:
        print(f_content, end= '*')
        f_content = f.read(size_to_read)

with open('file2.txt', 'w') as f:
    pass

# f = open('file.txt', 'r')
# print(f.name)
# print(f.mode)

# print(f.readline(), end='')
# print(f.read())
# f.close()
