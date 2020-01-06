# copy from one file to another

# with open('file.txt', 'r') as rf:
#     with open('file2.txt', 'a') as wf:
#         for line in rf:
#             wf.write(line)

# now for having more control

with open('file.txt', 'r') as rf:
    with open('file2.txt', 'w') as wf:
        chunk_size = 100
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


