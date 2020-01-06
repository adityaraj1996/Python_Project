inputf = r"C:\Users\ARAJ17\Documents\F6744DEV.SPUFI.OUTPUT.txt"

outputc = ""
with open(inputf, "r+") as fin:
    for line in fin:
        arr = line.split(" ")
        outputc += arr[0] + "\n"

outputf = r"C:\Users\ARAJ17\Documents\F6744DEV.SPUFI.OUTPUT2.txt"
with open(outputf, "w+") as fout:
    fout.write(outputc)
