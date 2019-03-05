import sys
import test
from matplotlib import pyplot as plt

numbers = [0, 100, 200, 400, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000]
sys.setrecursionlimit(10000)
risultati = test.runAllTests(numbers)
for ris in risultati:
    print(ris)

x = [ris[0] for ris in risultati]


y = []
f, axarr = plt.subplots(2, sharex=True)
axarr[0].set_title("Altezza alberi")
y.append([ris[1] for ris in risultati])
axarr[0].plot(x, y[-1], label='ABR (ordinato)', color='blue')
axarr[0].legend(loc="upper left")

y.append([ris[2] for ris in risultati])
axarr[1].plot(x, y[-1], label='ARN (ordinato)', color='black')
y.append([ris[3] for ris in risultati])
axarr[1].plot(x, y[-1], label='ABR (migliore)', color='C0')  # celestino
y.append([ris[4] for ris in risultati])
axarr[1].plot(x, y[-1], label='ARN (migliore)', color='green')
y.append([ris[5] for ris in risultati])
axarr[1].plot(x, y[-1], label='ABR (random)', color='C1')  # giallo
y.append([ris[6] for ris in risultati])
axarr[1].plot(x, y[-1], label='ARN (random)', color='red')

axarr[1].legend(loc="upper left")
plt.show()

f, axarr = plt.subplots(2, sharex=True)
axarr[0].set_title("Tempo di inserimento")
y.append([ris[7] for ris in risultati])
axarr[0].plot(x, y[-1], label='ABR (ordinato)', color='blue')
axarr[0].legend(loc="upper left")

y.append([ris[8] for ris in risultati])
axarr[1].plot(x, y[-1], label='ARN (ordinato)', color='black')
y.append([ris[9] for ris in risultati])
axarr[1].plot(x, y[-1], label='ABR (migliore)', color='C0')  # celestino
y.append([ris[10] for ris in risultati])
axarr[1].plot(x, y[-1], label='ARN (migliore)', color='green')
y.append([ris[11] for ris in risultati])
axarr[1].plot(x, y[-1], label='ABR (random)', color='C1')  # giallo
y.append([ris[12] for ris in risultati])
axarr[1].plot(x, y[-1], label='ARN (random)', color='red')

axarr[1].legend(loc="upper left")
plt.show()
