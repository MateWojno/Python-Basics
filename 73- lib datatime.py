import datetime

teraz = datetime.datetime.now()
print(teraz)
print(teraz.ctime)

miesiac = str(teraz.month)

dzien = str(teraz.day)

rok = str(teraz.year)

godzina = str(teraz.hour)

minuta = str(teraz.minute)

sekunda = str(teraz.second)

print (dzien + "." + miesiac + '.' + rok + '.'+ godzina + '.' + minuta + '.' +sekunda)