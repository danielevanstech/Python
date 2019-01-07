#Test to see if this works right
test = 'test'
cidrDict = {
	'24':'255.255.255.0',
	'16':'255.255.0.0',
	'8':'255.0.0.0'
}
x = 0
ipAddr = input('What is the ip address?')
while x == 0:
	cidr = input('What is the CIDR?')
	if cidr in cidrDict:
		print('Your CIDR has been found, continuing...')
		x += 1
	else:
		print('----------\nCIDR not found, try again\n----------')