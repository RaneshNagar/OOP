file = open ('text.txt')
print(file.read())
file.close()

file1 = open('text.txt','w')
file1.write("Hello wrold")
file1.close()

file2 = open('text.txt','a')
file2.write('append')
file2.close()
