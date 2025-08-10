req = input()
req = req.replace(' ', '')


def find_signs(line, sign):
    start = 0
    m = []
    for _ in line:
        i = line.find(sign, start)
        if i == -1:
            break
        m.append(i)
        start = i + 1
    return m


def get_cur_next(t_list, t_i, req):
    t_len = len(t_list)
    r_len = len(req)
    if t_i < t_len:
        t_c = t_list[t_i]
        t_n = t_list[t_i + 1] if t_i + 1 < t_len else r_len
    else:
        t_c = r_len
        t_n = r_len

    return t_c, t_n


p_list = find_signs(req, '+')
m_list = find_signs(req, '-')

# cur = 0
p_i = 0
m_i = 0
p = req.find('+')
m = req.find('-')
cur = min(p, m)
if cur == -1:
    cur = max(p, m)
calc = int(req[0:cur])
while True:
    p, pn = get_cur_next(p_list, p_i, req)
    m, mn = get_cur_next(m_list, m_i, req)
    c_min = min(p, m)
    c_max = max(p, m)
    n_min = min(pn, mn)
    next_c = c_max if c_max < n_min else n_min

    # no more ops to do
    if c_min == len(req):
        break

    next_num = int(req[c_min + 1:next_c])
    calc += next_num if p < m else (0 - next_num)

    if p < m:
        p_i += 1
    else:
        m_i += 1

print(calc)
