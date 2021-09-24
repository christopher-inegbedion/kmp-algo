import timeit
import matplotlib.pyplot as plt


def _build_table(text) -> list:
    table = [0 for i in range(len(text))]

    i = 0
    j = 1

    for k in range(len(table)-1):
        val_i = text[i]
        val_j = text[j]

        if val_i == val_j:
            table[j] = i+1
            i = i+1
            j = j+1
        else:
            i = 0
            j = j+1

    return table


def kmp_search(p, w):
    table = _build_table(p)

    p_pos = 0
    for i in w:
        if p_pos == len(p)-1:
            return True

        # print(p_pos)
        if p[p_pos] == i:
            p_pos = p_pos+1
        else:
            table_val = table[p_pos-1]
            p_pos = 0+table_val

    return False


def search(pat, txt):
    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1

        # if (j == M):
        #     print("Pattern found at index ", i)


w = "inegbedion eromosele"
p = "eromho"

# print(_build_table(p))

kmp_data = [
    [kmp_search for i in range(1)],
    [kmp_search for i in range(10)],
    [kmp_search for i in range(100)],
    [kmp_search for i in range(1000)],
    [kmp_search for i in range(10000)],
    [kmp_search for i in range(100000)],
    [kmp_search for i in range(1000000)],
    # [kmp_search for i in range(10000000)],
    # [kmp_search for i in range(100000000)],
]

naive_data = [
    [search for i in range(1)],
    [search for i in range(10)],
    [search for i in range(100)],
    [search for i in range(1000)],
    [search for i in range(10000)],
    [search for i in range(100000)],
    [search for i in range(1000000)],
    # [search for i in range(10000000)],
    # [search for i in range(100000000)],
]

naive_times = []
kmp_times = []

kmp_iters = {
    "iters": [],
    "time_taken": []}

naive_iters = {
    "iters": [],
    "time_taken": []
}

iters = 0
for i in kmp_data:
    start = timeit.default_timer()
    for j in i:
        j(p, w)
    stop = timeit.default_timer()
    kmp_iters["iters"].append(len(i))
    kmp_iters["time_taken"].append(stop-start)
    iters = iters+1

iters = 0
for i in naive_data:
    start = timeit.default_timer()
    for j in i:
        j(p, w)
    stop = timeit.default_timer()
    naive_iters["iters"].append(len(i))
    naive_iters["time_taken"].append(stop-start)
    iters = iters+1


ax = plt.subplot()
ax.plot(naive_iters["iters"], naive_iters["time_taken"], label="naive")
ax.plot(kmp_iters["iters"], kmp_iters["time_taken"], label="kmp")
# df.plot(kmp_iters, x="iters", y="time_taken")
plt.legend()
plt.show()
