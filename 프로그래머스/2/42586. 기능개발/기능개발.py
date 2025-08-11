from math import ceil

def solution(progresses, speeds):
    answer = []
    days = [ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    count = 1
    day = days[0]

    for i in range(1, len(days)):
        if day < days[i]:
            answer.append(count)
            count = 1
            day = days[i]
        else:
            count += 1
    
    answer.append(count)

    return answer