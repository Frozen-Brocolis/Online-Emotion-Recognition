
import random
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pylab
class Grafik():
    def __init__(self):
        self.x = []
        self.angry=[]
        self.disgust=[]
        self.fear = []
        self.happy = []
        self.sad = []
        self.surprise=[]
        self.neutral = []
        pylab.grid(True)

    def update(self,time,data):

        #Обновляем данные
        self.x.append(time)

        self.angry.append(data["angry"])
        self.surprise.append(data["surprise"])
        self.neutral.append(data["neutral"])
        self.sad.append(data["sad"])
        self.disgust.append(data["disgust"])
        self.fear.append(data["fear"])
        self.happy.append(data["happy"])

        names=[]
        N=[]
        for i in data:
            names.append(i)
            N.append(data[i])

        # Рисуем

        pylab.subplot(2, 2, 1)
        pylab.cla()
        pylab.plot(self.x[-100:], self.angry[-100:],label=u"angry")
        pylab.plot(self.x[-100:], self.disgust[-100:],label=u"disgust")
        pylab.plot(self.x[-100:], self.fear[-100:],label=u"fear")
        pylab.plot(self.x[-100:], self.happy[-100:],label=u"happy")
        pylab.plot(self.x[-100:], self.sad[-100:],label=u"sad")
        pylab.plot(self.x[-100:], self.surprise[-100:],label=u"surprise")
        pylab.plot(self.x[-100:], self.neutral[-100:],label=u"neutral")
        pylab.title ('График эмоций')




        pylab.subplot(2, 2, 2)
        pylab.cla()
        pylab.pie(N,labels=names)
        pylab.title("Соотношение эмоций")

        pylab.subplot(2, 2, 3)
        pylab.cla()
        pylab.bar(names,N)
        pylab.title("Соотношение эмоций 2")
        plt.pause(0.1)
    def load(self):
        plt.show()
