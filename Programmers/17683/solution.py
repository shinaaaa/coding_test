def convert(text: str):
    text = text.replace("C#", "H")
    text = text.replace("D#", "I")
    text = text.replace("F#", "J")
    text = text.replace("G#", "K")
    text = text.replace("A#", "L")

    return text


def solution(m, musicinfos):
    answer = ''
    m = convert(m)

    musicinfos_ = list(item.split(",") for item in musicinfos)
    info = ["", 0]

    for item in musicinfos_:
        start = item[0]  # 시작 시간
        end = item[1]  # 종료시간
        title = item[2]  # 제목
        m_list = convert(item[3])  # 음 리스트
        m_loop = ""

        # 시간 계산
        end_t = list(map(int, end.split(":")))
        start_t = list(map(int, start.split(":")))
        e = end_t[0] * 60 + end_t[1]
        s = start_t[0] * 60 + start_t[1]

        play_time = e - s

        if play_time > len(m_list):
            while play_time >= len(m_loop):
                m_loop += m_list
        else:
            m_loop = m_list

        time_ = m_loop[:play_time]

        if time_.find(m) > -1:
            c = m_loop.find(m)
            if info[1] < play_time:
                info[0] = title
                info[1] = play_time

        if info[0] == "":
            answer = "(None)"
        else:
            answer = info[0]
    return answer
