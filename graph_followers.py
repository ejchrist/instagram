#! /usr/bin/python2.7

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import datetime

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

today = datetime.datetime.now().strftime("%Y%m%d")

def animate(i):
    pullData = open(today + "stats.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
