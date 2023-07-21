import os

newfile = open("help/usebrain.txt", "w")

with open("help/piplist.txt", 'r') as file_data:
    for line in file_data:
        data = line.split(" ", 1)
        #print(data)
        newfile.write(data[0] + "==" + data[1])
newfile.close()
