import json
from bson import json_util

data = {"nome": "hugo", "idade":31}
data = json.dumps(data).encode('utf-8')

print(type(data))
print(data)

data = data.decode('utf-8')
print(type(data))
print(data)