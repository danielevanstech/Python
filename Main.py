cidrDict = {
	'24':'255.255.255.0',
	'16':'255.255.0.0',
	'8':'255.0.0.0'
}
x = 0
ipAddr = input('What is the starting IP address of your range?')
cidr = input('What is the CIDR of the network you want to scan?')
netMask = cidrDict[str(cidr)]