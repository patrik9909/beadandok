def szamlalo(datum):
      from datetime import datetime
      datumkon=datum.split("-")
      l=[]
      date_format = "%Y/%m/%d/"
      ido = datetime(int(datumkon[0]), int(datumkon[1]), int(datumkon[2]))
      miku = datetime(2019, 12, 6)
      delta = miku - ido
      final= delta.days
      l.append(final)
      print(l[0],"napot kell még aludni mikulásig")
print(timer("2015-02-07"))

