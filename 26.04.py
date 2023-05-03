def get_data():
    import random
    n = 100
    m = 100
    inp_arr = [[True for i in range(n)] if j == 0 else [False for i in range(n)] for j in range(m)]
    
    w = [[random.uniform(0, 0.3) for j in range(n)] for i in range(n)]

    d = [[random.randint(1, 3) for j in range(n)] for i in range(n)]


    return inp_arr, w, d

def network(inp, w, d):
    import matplotlib.pyplot as plt
    import numpy as np 

    out = []
    u = [0  for i in range(len(w))]
    # tau = 10 
    # arr = []
    
    for i in range(len(inp)):
        out.append([])
        for j in range(len(w)):
            # new_u = u[j] * (1 - 1/tau)
            # print(new_u)
            # if new_u > 1:
            #     new_u = True
            # else:
            #     new_u = False

            # out[i].append(new_u)  

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
    inp_arr, w, d = get_data()
    out = network(inp_arr, w, d)
    # for row in out:
    #     print(sum(row))
    draw(out)


if __name__ == "__main__":
    main()