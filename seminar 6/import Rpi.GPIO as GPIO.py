import RPi.GPIO as GPIO
import time 
import matplotlib.pyplot as plt 
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
t = 0
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
def voltage():
    print(adc())
    return(GPIO.input(troyka))
def binary(x):
    return[int(n) for n in bin(x)[2:].zfill(8)]
def g():
    GPIO.output(led, binary(voltage()))
def adc():
    x = 0 
    for i in range(7, -1, -1):
        n = 2**i
        x += n 
        sbinary = binary(x)
        GPIO.output(dac, sbinary)
        time.sleep(0.01)
        if GPIO.input(comp) == 1:
            x -= n
    return(x)
t1 = time.time()
try:
    n = []
    GPIO.output(troyka, 11111111)
    while adc() < 207:
        voltage()
        n.append(adc())
        t+= 0.01
        time.sleep(0.01)
    GPIO.output(troyka, 0)
    while adc() > 176:
        voltage()
        n.append(adc())
        t+= 0.01
        time.sleep(0.01)

    strn = [str(item) for item in n]
    stra = [str(item) for item in [1000, 0.013]]
    t2 = time.time()
    t = t2-t1
    print(t)
    print(t/len(n))
    print(len(n)/t)
    print(3.3/256)
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(strn))
    with open("settings.txt", "w") as file:
        file.write(str([str(item) for item in [len(n)/t, 3.3/256]]))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac) 
plt.plot(n)
plt.show()

    



    
    



