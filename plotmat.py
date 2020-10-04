import matplotlib.pyplot as plt
from textwrap import wrap

def plotfig(chromosome,filename):
    x = [x[1][0] for x in chromosome]
    y = [y[1][1] for y in chromosome]
    x0 = [x[1][0] for x in chromosome if x[0]=='h' ]
    x1 = [x[1][0] for x in chromosome if x[0]=='p' ]
    y0 = [y[1][1] for y in chromosome if y[0]=='h' ]
    y1 = [y[1][1] for y in chromosome if y[0]=='p' ]
    plt.title("\n".join(wrap('wyerieywroieirytyertyoirytyroytyerotyertrdsfsdfsdfsdfsdfsdfsdffffffffffffffffffffffffffffffffffff',60)))
    plt.plot(x,y,linewidth=3.0)
    hmarker = dict(color='0',marker='o',markersize=10,linewidth=0,label='h')
    plt.plot(x0,y0,**hmarker)
    pmarker = dict(color='0',marker='o',markersize=10,fillstyle='none',linewidth=0,label='p')
    plt.plot(x1,y1,**pmarker)
    plt.grid(True)
    # plt.show()
    plt.legend(loc="best")
    plt.savefig('figure-%s'%(str(filename)))
    plt.close()
chromosomes =  [[('h', (0, 0)), ('p', (0, -1)), ('h', (0, -2)), ('p', (-1, -2)), ('p', (-1, -1)), ('h', (-1, 0)), ('h', (-1, 1)), ('p', (-1, 2)), ('h', (0, 2)), ('p', (1, 2)), ('p', (1, 3)), ('h', (0, 3)), ('p',
(-1, 3)), ('h', (-2, 3)), ('h', (-3, 3)), ('p', (-4, 3)), ('p', (-5, 3)), ('h', (-5, 4)), ('p', (-6, 4)), ('h', (-6, 3))]
,
[('h', (0, 0)), ('p', (0, -1)), ('h', (0, -2)), ('p', (-1, -2)), ('p', (-1, -1)), ('h', (-1, 0)), ('h', (-1, 1)), ('p', (-1, 2)), ('h', (0, 2)), ('p', (1, 2)), ('p', (1, 3)), ('h', (0, 3)), ('p',
(-1, 3)), ('h', (-2, 3)), ('h', (-2, 2)), ('p', (-2, 1)), ('p', (-2, 0)), ('h', (-3, 0)), ('p', (-3, -1)), ('h', (-2, -1))]
]
for idx,chromosome in enumerate(chromosomes):
    plotfig(chromosome,idx)
    