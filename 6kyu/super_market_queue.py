def queue_time(customers, n):
    lines = [0] * n
    for x in customers:
        lines.sort()
        lines[0] += x
    return max(queues)

def queue_time(customers, n):
    lines = [0] * n
    time = 0
    for x in customers:
        lines.sort(reverse=True)
        lines[-1] += x
    return lines


    for x in customers:
        lin
    while len(customers) > 0 or sum(lines) > 0:
        for i in range(len(cashiers)):
            if lines[i] == 0 and len(customers) > 0:
                lines[i] = customers.pop(0)
            if lines[i] > 0:
                lines[i] -= 1
        time += 1
    return time
