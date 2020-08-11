import sys, time
import backend

sys.stdout.write('\rNOTICE: This version of the live coronavirus updater is very basic and has very limiting controls.')
time.sleep(4)

while True:
    sys.stdout.write('\rGlobal Cases: ' + format(backend.cases()))
    time.sleep(5)
    sys.stdout.write('\rGlobal Deaths: ' + format(backend.deaths()))
    time.sleep(5)
    sys.stdout.write('\rGlobal Recoveries: ' + format(backend.recoveries()))
    time.sleep(5)