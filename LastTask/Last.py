class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


def max_meeting(l, n):
    l.sort(key=lambda x: x.end)
    max_counter = 0
    for i in range(n):
        counter = 0
        for j in range(i, n):
            if l[j].start < l[i].end:
                counter += 1
        if counter > max_counter:
            max_counter = counter
    print(max_counter)


def get_max(span):
    s = [elem[0] for elem in span]
    f = [elem[1] for elem in span]
    l = []
    for i in range(len(s)):
        l.append(meeting(s[i], f[i], i))
    return max_meeting(l, len(s))


get_max([[2, 10], [3, 4], [6, 9]])
get_max([[1, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [5, 6]])
get_max([[1, 8], [2, 7], [3, 5], [5, 7], [6, 7], [6, 8], [7, 8]])
