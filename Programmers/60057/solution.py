def solution(s):
    answer = 0

    length = len(s)

    if length == 1:
        return 1

    for i in range(1, length):
        target = s[0:i]
        start = i
        end = i + i
        arr = {target: 1}
        result = ""

        while end <= length:
            item_ = s[start:end]

            if item_ == target:
                arr[item_] = arr[item_] + 1
            else:
                if arr[target] > 1:
                    result += str(arr[target])
                result += target

                target = item_
                arr[target] = 1

            start += i
            end += i

        if arr[target] > 1:
            result += str(arr[target])
        result += target

        if start + i > length:
            result += s[start:]

        if answer == 0:
            answer = len(result)
        elif answer >= len(result):
            answer = len(result)

    return answer
