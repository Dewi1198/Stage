files = ['hallo.docx', 'test.xml', 'test.7z.001']

for file in files:
	x = str(file).split('/')[-1].lower()
	
	if x.count('.') == 1:
		current = x.split('.')[-1]
		extlen = len(current)
		print ('Extensie:', current)
		print ('Lengte:', extlen)
		print ()

	if x.count('.') == 2:
		current = x.split('.', 1)[-1]
		extlen = len(current)
		print ('Extensie:', current)
		print ('Lengte:', extlen)
		print ()
