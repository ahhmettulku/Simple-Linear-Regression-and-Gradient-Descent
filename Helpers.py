import numpy as np
import matplotlib.pyplot as plt

# draw derivative line
# y = m*(x - x1) + y1
def add_line(dj_dx, x1, y1, d, ax):
    x = np.linspace(x1-d, x1+d,50)
    y = dj_dx*(x - x1) + y1
    ax.scatter(x1, y1, color='#0096ff', s=50)
    ax.plot(x, y, '--', c='#C00000',zorder=10, linewidth = 1)
    xoff = 30 if x1 == 200 else 10
    ax.annotate(r"$\frac{\partial J}{\partial w}$ =%d" % dj_dx, fontsize=14,
                xy=(x1, y1), xycoords='data',
            xytext=(xoff, 10), textcoords='offset points',
            arrowprops=dict(arrowstyle="->"),
            horizontalalignment='left', verticalalignment='top')
    
def plt_gradients(x_train,y_train, f_compute_cost, f_compute_gradient):
    fig,ax = plt.subplots(figsize=(8,4))

    # Print w vs cost to see minimum
    fix_b = 100
    #w_array = np.linspace(-100, 500, 50)
    w_array = np.linspace(0, 400, 50)
    cost = np.zeros_like(w_array)

    for i in range(len(w_array)):
        tmp_w = w_array[i]
        cost[i] = f_compute_cost(x_train, y_train, tmp_w, fix_b)
    ax.plot(w_array, cost,linewidth=1)
    ax.set_title("Cost vs w, with gradient; b set to 100")
    ax.set_ylabel('Cost')
    ax.set_xlabel('w')

    # plot lines for fixed b=100
    for tmp_w in [100, 200, 300]:
        fix_b = 100
        dj_dw,dj_db = f_compute_gradient(x_train, y_train, tmp_w, fix_b )
        j = f_compute_cost(x_train, y_train, tmp_w, fix_b)
        add_line(dj_dw, tmp_w, j, 30, ax)