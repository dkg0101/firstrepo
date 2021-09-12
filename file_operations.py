# 1)
f = open("lyrics.txt", "r") # f is called file pointer
action= f.read()
print(action)
"""
we can also read / print it as,
for line in f :
    print(line,end="")
"""
f.close() #file opened must has to close

import sys
sys.exit(0)
# 2)
f = open("lyrics.txt", "r") # f is called file pointer
print(f.readline()) #f.readline will read new line charecter
print(f.readline())
f = open("lyrics.txt", "r") # f is called file pointer


import sys
sys.exit(0)
# 3)

f = open("lyrics.txt", "r") # f is called file pointer
print(f.readlines()) #f.readlines will store the lines in list


import sys
sys.exit(0)
# 3)
f = open("lyrics2","w") # f is called file pointer

j = f.write("This function will clears all previous data in this particular file and write fresh once")
# print(j)
f.close()

import sys
sys.exit(0)
# 4)
f = open("lyrics2", "r+")
both = f.write("This line has written by using read+write both function")
# f = open("lyrics2","a")
# append = f.write("\nThis text is appended !")

import sys
sys.exit(0)

# 5) block method
with open ("lyrics3.txt","r+") as f :
       k = f.read()
       print(k)







