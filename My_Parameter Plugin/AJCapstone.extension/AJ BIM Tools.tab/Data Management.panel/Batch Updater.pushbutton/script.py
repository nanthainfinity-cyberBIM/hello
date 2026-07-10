import os
import base64
import zlib
from pyrevit import forms

folder_path = os.path.dirname(__file__)
source_file = os.path.join(folder_path, "source_code.py")
output_file = os.path.join(folder_path, "script_locked.py")

try:
    # 1. Read your master code
    with open(source_file, 'r') as f:
        code_text = f.read()
        
    # 2. Scramble and encrypt the code
    compressed_code = zlib.compress(code_text.encode('utf-8'))
    encrypted_string = base64.b64encode(compressed_code).decode('utf-8')
    
    # 3. Build the locked runner script
    locked_code = "# -*- coding: utf-8 -*-\n"
    locked_code += "import base64\nimport zlib\n"
    locked_code += "exec(zlib.decompress(base64.b64decode('{}')).decode('utf-8'))".format(encrypted_string)
    
    # 4. Save the new locked file
    with open(output_file, 'w') as f:
        f.write(locked_code)
        
    forms.alert("Encryption Success! Look for 'script_locked.py' in your folder.")
except Exception as e:
    forms.alert("Error: " + str(e))
    #Change
