file1 = open('Джамалов Дмитрий Максимович_УБ-42_vvod.txt', 'r')
file2 = open('Джамалов Дмитрий Максимович_УБ-42_vivod.txt', 'r+')
a = file1.read()
file2.write(a)