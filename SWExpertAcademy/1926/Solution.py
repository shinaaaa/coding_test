T = int(input())
result = []
for num in range(1, T + 1):
    text1 = str(num)
    text2 = (str(num).replace('3', '-')
             .replace('6', '-')
             .replace('9', '-'))
    if(text1 != text2):
        if(text2.count('-') == 1):
            result.append('-')
        else:
            result.append(text2)
    else:
        result.append(text2)

for i in range(len(result)):
    print(result[i], end=' ')
