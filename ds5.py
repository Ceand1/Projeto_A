import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

indx = 10
apply_weight_adjustment = True  

def generate_ind7(val):
    return np.linspace(0, val, 100)


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.5) 

ind7 = generate_ind7(0)

def calculate_averages(ind7, b):
    p = ((1-b)/10) * ind7 + b
    ari3 = [(p[i] * ind7[i] + 9 * indx)/(9+p[i]) for i in range(len(ind7))]
    geo3 = [((ind7[i]**p[i] * indx**9)**(1 / (p[i] + 9))) for i in range(len(ind7))]
    har3 = [( (p[i] + 9) / ((p[i] / ind7[i]) + (9 / indx))) for i in range(len(ind7))]

    ari4 = [(ind7[i] + 9*indx)/10 for i in range(len(ind7))]
    geo4 = [(pow(ind7[i] * indx**9, 1/10)) for i in range(len(ind7))]
    har4 = [(10/((1/ind7[i])+(9/indx))) for i in range(len(ind7))]

    return ari3, geo3, har3, ari4, geo4, har4

b_init = 2

ari3, geo3, har3, ari4, geo4, har4 = calculate_averages(ind7, b_init)

l1, = plt.plot(ind7, ari3, label="MP - Peso Variável", color='blue')
l2, = plt.plot(ind7, geo3, label="MG - Peso Variável", color='green')
l3, = plt.plot(ind7, har3, label="MH - Peso Variável", color='red')

l4, = plt.plot(ind7, ari4, label="MP", color='orange')
l5, = plt.plot(ind7, geo4, label="MG", color='black')
l6, = plt.plot(ind7, har4, label="MH", color='purple')

plt.ylim(0, 13)
plt.xlim(0, 11)
plt.xlabel("IND7")
plt.ylabel("IQS")
plt.title("IQS-Média Ponderada X Média Geométrica X Média Harmônica")
plt.legend(loc='lower right')


axcolor = 'lightgoldenrodyellow'
axind7 = plt.axes([0.1, 0.25, 0.8, 0.03], facecolor=axcolor)
slider = Slider(axind7, 'IND7', 0, 10, valinit=0)

axcolor = 'lightgoldenrodyellow'
axb = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axcolor)
sliderb = Slider(axb, 'b', 2, 10, valinit=b_init)

def update(val):
    new_end = slider.val  
    ind7 = np.linspace(0, new_end, 100)
    b = sliderb.val
    
    ari3, geo3, har3, ari4, geo4, har4 = calculate_averages(ind7, b)

    if apply_weight_adjustment:
        l1.set_xdata(ind7)
        l2.set_xdata(ind7)
        l3.set_xdata(ind7)

        l4.set_xdata(ind7)
        l5.set_xdata(ind7)
        l6.set_xdata(ind7)

        l1.set_ydata(ari3)
        l2.set_ydata(geo3)
        l3.set_ydata(har3)

        l4.set_ydata(ari4)
        l5.set_ydata(geo4)
        l6.set_ydata(har4)
    
    else:
        l4.set_xdata(ind7)
        l5.set_xdata(ind7)
        l6.set_xdata(ind7)

        l4.set_ydata(ari4)
        l5.set_ydata(geo4)
        l6.set_ydata(har4)

    ax.relim()  
    ax.autoscale_view() 
    
    fig.canvas.draw_idle()

axbutton = plt.axes([0.1, 0.05, 0.2, 0.04])
button = Button(axbutton, '', color=axcolor, hovercolor='0.975')

def toggle_weight_adjustment(event):
    global apply_weight_adjustment
    apply_weight_adjustment = not apply_weight_adjustment
    update(slider.val)

button.on_clicked(toggle_weight_adjustment)

slider.on_changed(update)
sliderb.on_changed(update)

plt.show()
