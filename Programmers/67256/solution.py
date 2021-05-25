def solution(numbers, hand):
    answer = ''

    l_hand = Position(3, 0)
    r_hand = Position(3, 2)

    for l in numbers:
        s = getHand(l)
        x, y = getPosition(l)
        if s == '':
            l_c = abs(l_hand.x - x) + abs(l_hand.y - y)
            r_c = abs(r_hand.x - x) + abs(r_hand.y - y)

            if l_c > r_c:
                s = 'R'
            elif l_c < r_c:
                s = 'L'
            else:
                if hand == 'right':
                    s = 'R'
                else:
                    s = 'L'
        if s == 'R':
            r_hand.x = x
            r_hand.y = y
        else:
            l_hand.x = x
            l_hand.y = y

        answer += s

    return answer


def keypad(x, y):
    location = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', 0, '#']]

    return location[x][y]


def getPosition(pos):
    pos = str(pos)
    dict = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
            '4': (1, 0), '5': (1, 1), '6': (1, 2),
            '7': (2, 0), '8': (2, 1), '9': (2, 2),
            '*': (3, 0), '0': (3, 1), '#': (3, 2)}

    return dict[pos][0], dict[pos][1]


def getHand(pos):
    pos = str(pos)
    dict = {'1': 'L', '2': '', '3': 'R',
            '4': 'L', '5': '', '6': 'R',
            '7': 'L', '8': '', '9': 'R',
            '*': 'L', '0': '', '#': 'R'}

    return dict[pos]


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y