import sys, time
import backend as bk

while True:
    cases, deaths, recovered = bk.data_return()
    sys.stdout.write('\rGlobal Cases: ' + format(cases))
    time.sleep(5)
    sys.stdout.write('\rGlobal Deaths: ' + format(deaths))
    time.sleep(5)
    sys.stdout.write('\rGlobal Recoveries: ' + format(recovered))
    time.sleep(5)
