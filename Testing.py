f = open('Main.py')
for line in f:
    findMe = 'cidrDict'
    x = line.__contains__(findMe)
    print(x,'found in this line',line)