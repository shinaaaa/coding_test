# 문제 유형 : 해시, 구현

import hashlib

input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()

print(result)
