def solution(s):
    splitarr = s.split(" ")
    answer = []
    for c in splitarr:
        if c:
            if c[0].isdigit():
                stritem = c[0] + c[1:].lower()
            else:
                stritem = c.capitalize()
        else:
            stritem = c

        answer.append(stritem)

    return ' '.join(answer)