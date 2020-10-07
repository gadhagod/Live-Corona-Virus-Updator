import backend

cases, deaths, recoveries = backend.data_return()

print('Cases: ' + str(cases))
print('Deaths: ' + str(deaths))
print('Recoveries: ' + str(recoveries))
