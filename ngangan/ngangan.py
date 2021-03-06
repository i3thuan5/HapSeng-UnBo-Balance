import csv

with open(
        '名姓字表 - 字姓.csv') as tong:
        reader = csv.reader(tong)
        next(reader, None)
        senn = []
        for pit in reader:
            senn.append(pit[2])


with open(
        '名姓字表 - 人名.csv') as tong:
        reader = csv.reader(tong)
        next(reader, None)
        senn_dict = {}
        ngangan_w = []
        ngangan_p = []
        for pit in reader:
            if '(文)' in pit[1]:
                ngangan_w.append(pit[0])
            if '(白)' in pit[1] or '(不標)' in pit[1]:
                ngangan_p.append(pit[0])
        print(ngangan_w, ngangan_p)


for index in range(0, 400, 2):
    print(senn[index % 100], 'X', ngangan_w[index*2])
    print(senn[(1+index) % 100], ngangan_w[1+index*2], 'X')
    print('X', ngangan_w[2+index*2])
    print(ngangan_w[3+index*2], 'X')

fout = open('ngangan_w.txt', 'w')
for index in range(0, 400, 2):
    fout.write(senn[index % 100] + 'X' + ngangan_w[index*2] + '\n')
    fout.write(senn[(1+index) % 100] + ngangan_w[1+index*2] + 'X'+ '\n')
    fout.write('X' + ngangan_w[2+index*2]+ '\n')
    fout.write(ngangan_w[3+index*2] + 'X'+ '\n')
fout.close()


for index in range(0, 400, 2):
    print(senn[index % 100], 'X', ngangan_p[index*2])
    print(senn[(1+index) % 100], ngangan_p[1+index*2], 'X')
    print('X', ngangan_p[2+index*2])
    print(ngangan_p[3+index*2], 'X')

fout = open('ngangan_p.txt', 'w')
for index in range(0, 400, 2):
    fout.write(senn[index % 100] + 'X' + ngangan_p[index*2] + '\n')
    fout.write(senn[(1+index) % 100] + ngangan_p[1+index*2] + 'X'+ '\n')
    fout.write('X' + ngangan_p[2+index*2]+ '\n')
    fout.write(ngangan_p[3+index*2] + 'X'+ '\n')
fout.close()

fout = open('ngangan_w1.txt', 'w')
for index in range(0, 400, 2):
    fout.write(senn[index % 100] + 'X' + ngangan_w[index*2] + '\n')
fout.close()

fout = open('ngangan_w2.txt', 'w')
for index in range(0, 400, 2):
    fout.write(senn[(1+index) % 100] + ngangan_w[1+index*2] + 'X'+ '\n')
fout.close()

fout = open('ngangan_w3.txt', 'w')
for index in range(0, 400, 2):
    fout.write('X' + ngangan_w[2+index*2]+ '\n')
fout.close()

fout = open('ngangan_w4.txt', 'w')
for index in range(0, 400, 2):
    fout.write(ngangan_w[3+index*2] + 'X'+ '\n')
fout.close()


fout = open('ngangan_p1.txt', 'w')
for index in range(0, 400, 2):
    fout.write(senn[index % 100] + 'X' + ngangan_p[index*2] + '\n')
fout.close()

fout = open('ngangan_p2.txt', 'w')
for index in range(0, 400, 2):
    fout.write(senn[(1+index) % 100] + ngangan_p[1+index*2] + 'X'+ '\n')
fout.close()

fout = open('ngangan_p3.txt', 'w')
for index in range(0, 400, 2):
    fout.write('X' + ngangan_p[2+index*2]+ '\n')
fout.close()

fout = open('ngangan_p4.txt', 'w')
for index in range(0, 400, 2):
    fout.write(ngangan_p[3+index*2] + 'X'+ '\n')
fout.close()