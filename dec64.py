import base64
import sys

code = sys.argv[1]

print(base64.b64decode(code))

