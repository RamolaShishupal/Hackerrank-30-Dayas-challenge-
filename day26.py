# Enter your code here. Read input from STDIN. Print output to STDOUT
# d1=input()
# d2=input()
# # print(d1,d2)
# a=d1.split(sep=' ')
# b=d2.split(sep=" ")
# # print(a,b)
# if a[-1]>b[-1]:
    
#     print("10000")
# elif a[-1]==b[-1] and a[1]==b[1] and b[0]<a[0]:
#     print(15*abs(int(a[0])-int(b[0])))
# elif a[-1]==b[-1] and a[1]>b[1]:
#     print(500*abs(int(a[1])-int(b[1])))
# else:
#     print("0")
    

# print(10000 if a[2]>e[2] else
#     500*(a[1]-e[1]) if a[2]==e[2] and a[1]>e[1] else
#     15*(a[0]-e[0]) if a[2]==e[2] and a[1]==e[1] and a[0]>e[0] else 0)
import sys

def split_input_line(a_line):
    components = a_line.split(" ")
    for i in range(3):
        components[i] = int(components[i])
    return components

input_line1 = sys.stdin.readline().strip()
input_line2 = sys.stdin.readline().strip()

d1, m1, y1 = split_input_line(input_line1)
d2, m2, y2 = split_input_line(input_line2)

#print("d m y {} {} {}".format(d1, m1, y1))
#print("d m y {} {} {}".format(d2, m2, y2))

if y1 > y2:
    print(10000)
elif y1 == y2 and m1 > m2:
    print(500 * (m1 - m2))
elif y1 == y2 and m1 == m2 and d1 > d2:
    print(15 * (d1 - d2))
else:
    print(0)
