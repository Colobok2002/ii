
def get_data():
    import random
    Nn = 100
    Ni = 10
    inp_arr = [[True for i in range(Nn)] if j == 0 else [False for i in range(Nn)] for j in range(Ni)]

    wi = [[random.uniform(0, 0.2) for j in range(Nn + Ni)] for i in range(Nn)]

    wpp = [[random.uniform(0, 0.2) for j in range(Nn + Ni)] for i in range(Nn)]

    wpm = [[random.uniform(0, 0.2) for j in range(Nn + Ni)] for i in range(Nn)]

    wmp = [[random.uniform(0, -0.2) for j in range(Nn + Ni)] for i in range(Nn)]

    wmm = [[random.uniform(0, -0.2) for j in range(Nn + Ni)] for i in range(Nn)]

    di = [[random.randint(0, 1) for j in range(Nn + Ni)] for i in range(Nn)]

    dpp = [[random.randint(1, 1) for j in range(Nn + Ni)] for i in range(Nn)]

    dpm = [[random.randint(0, 1) for j in range(Nn + Ni)] for i in range(Nn)]

    dmp = [[random.randint(0, -1) for j in range(Nn + Ni)] for i in range(Nn)]

    dmm = [[random.randint(0, -1) for j in range(Nn + Ni)] for i in range(Nn)]

    re = [[random.uniform(0, 0.7) for j in range(Nn + Ni)] for i in range(Nn)]

    rpp = [[random.uniform(0, 0.7) for j in range(Nn + Ni)] for i in range(Nn)]

    rpm = [[random.uniform(0, 0.7) for j in range(Nn + Ni)] for i in range(Nn)]

    rmp = [[random.uniform(0, -0.7) for j in range(Nn + Ni)] for i in range(Nn)]

    rmm = [[random.uniform(0, -0.7) for j in range(Nn + Ni)] for i in range(Nn)]

    return inp_arr, wi, wpp, wpm, wmp, wmm, di, dpp, dpm, dmp, dmm, re, rpp, rpm, rmp, rmm

def network(inp, wpp, wpm, wmp, wmm, di, dpp, dpm, dmp, dmm, re, rpp, rpm, rmp, rmm):
    import matplotlib.pyplot as plt
    import numpy as np

    out = []
    u = [0 for i in range(len(w))]
    tau = 10
    # arr = [] i

    for i in range(len(inp)):
        out.append([])
        for j in range(len(w)):
            u[j] = u[j] * (1 - 1 / tau)
            for k in range(len(w[0])):
                if k < len(inp[0]):
                    delay = d[j][k]
                    if i >= delay:
                        is_spike = inp[i - delay][k]
                        if is_spike:
                            # arr.append(is_spike)
                            u[j] = u[j] + w[j][k]
                else:
                    delay = d[j][k]
                    if i >= delay:
                        is_spike = out[i - delay][k - len(inp[0])]
                        if is_spike:
                            u[j] = u[j] + w[j][k]
                            # arr.append(is_spike)
                # print(w[j][k])
            if u[j] > 1:
                out[-1].append(True)
                u[j] = 0
            else:
                out[-1].append(False)
    return out

def network_2(inp, r, d):
    import matplotlib.pyplot as plt
    import numpy as np

    out = []
    u = [0 for i in range(len(r))]
    tau = 10
    # arr = []

    for i in range(len(inp)):
        out.append([])
        for j in range(len(r)):
            u[j] = u[j] * (1 - 1 / tau)
            for k in range(len(r[0])):
                if k < len(inp[0]):
                    delay = d[j][k]
                    if i >= delay:
                        is_spike = inp[i - delay][k]
                        if is_spike:
                            # arr.append(is_spike)
                            u[j] = u[j] + r[j][k]
                else:
                    delay = d[j][k]
                    if i >= delay:
                        is_spike = out[i - delay][k - len(inp[0])]
                        if is_spike:
                            u[j] = u[j] + r[j][k]
                            # arr.append(is_spike)
                # print(w[j][k])
            if u[j] > 1:
                out[-1].append(True)
                u[j] = 0
            else:
                out[-1].append(False)
    return out

def draw(data):
    import matplotlib.pyplot as plt
    import numpy as np

    # convert Boolean values to integers
    data = np.array(data, dtype=int)

    # plot heatmap
    plt.plot(data)

    # show plot
    plt.show()


def main():
    import matplotlib.pyplot as plt
    inp_arr, w, d, r = get_data()
    out = network(inp_arr, w, d)
    out_2 = network(inp_arr, r, d)
    for row in out:
        print(sum(row))
    # draw([sum(i) for i in out])
    plt.imshow(out)
    plt.show()
    plt.imshow(out_2)
    plt.show()


if __name__ == "__main__":
    main()


# Nn = 100
# Ni = 10
# Re = 0.7
# Di = 1
# Wi = 0.2
# wpp = 0.2
# wpm = 0.2
# wmp = 0.2
# wmm = 0.2
# Dpp = 1
# Dpm = 1
# Dmp = 1
# Dmm = 1
# Rpp = 0.3
# Rpm = 0.3
# Rmp = 0.3
# Rmm = 0.3