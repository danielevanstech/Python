file = open('Test.txt')
while True:
    char = file.read(1)
    if not char: break
    print(char)
for char in (open('Test.txt').read()): print(char)