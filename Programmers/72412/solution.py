import bisect


def solution(info, query):
    answer = []

    infos = [(list(item.split())) for item in info]

    dic = {}

    langs = ['cpp', 'java', 'python', '-']
    jobs = ['backend', 'frontend', '-']
    careers = ['junior', 'senior', '-']
    foods = ['chicken', 'pizza', '-']

    for lang in langs:
        for job in jobs:
            for career in careers:
                for food in foods:
                    dic[(lang, job, career, food)] = []

    for info in infos:
        dic[(info[0], info[1], info[2], info[3])].append(int(info[4]))

        dic[("-", "-", info[2], info[3])].append(int(info[4]))
        dic[("-", info[1], "-", info[3])].append(int(info[4]))
        dic[("-", info[1], info[2], "-")].append(int(info[4]))
        dic[(info[0], "-", "-", info[3])].append(int(info[4]))
        dic[(info[0], "-", info[2], "-")].append(int(info[4]))
        dic[(info[0], info[1], "-", "-")].append(int(info[4]))

        dic[("-", info[1], info[2], info[3])].append(int(info[4]))
        dic[(info[0], "-", info[2], info[3])].append(int(info[4]))
        dic[(info[0], info[1], "-", info[3])].append(int(info[4]))
        dic[(info[0], info[1], info[2], "-")].append(int(info[4]))

        dic[(info[0], "-", "-", "-")].append(int(info[4]))
        dic[("-", info[1], "-", "-")].append(int(info[4]))
        dic[("-", "-", info[2], "-")].append(int(info[4]))
        dic[("-", "-", "-", info[3])].append(int(info[4]))

        dic[("-", "-", "-", "-")].append(int(info[4]))

    for lang in langs:
        for job in jobs:
            for career in careers:
                for food in foods:
                    dic[(lang, job, career, food)].sort()

    querys = [(list(item.replace("and ", "").split())) for item in query]

    for item in querys:
        lang = item[0]
        job = item[1]
        career = item[2]
        food = item[3]
        score = item[4]

        arr = dic[(lang, job, career, food)]

        count = bisect.bisect_left(arr, int(score))

        answer.append(len(arr) - count)

    return answer
