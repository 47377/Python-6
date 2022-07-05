friuts = ("apple", "banana", "cherry")
print(friuts[0])
friuts = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(friuts[2:5])
print(friuts[:5])
print(friuts[2:])
#เพิ่มค่าในtuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#ลบค่าในtuple
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
#join
tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)
x = range(3, 6)
for n in x:
    print(n)
x = range(3, 20 , 5)
for n in x:
    print("rangeแบบstep2:",n)
    #นาย จิรัฏฐ์ แก่นคำ เลขที่ 6 ม.6/14