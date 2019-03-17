import re

text = '''

[dodoc](woo)


[dodocs](yeah)


[dodoc](hoo)


[dodoc](laa.hoo_8)

'''

print("1)")
output = re.sub('\[dodoc\]\(([\w\.]+)\)', lambda x: x.group(1) , text)
print(output)

print("2)")
for x in re.finditer('\[dodoc\]\(([\w\.]+)\)', text):
	full = x.group(0)
	item = x.group(1)
	print(full)
	print(item)
	
	print()
