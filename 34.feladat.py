try:

      infile=open("be.txt","r")
      outfile=open("output.py","w")
      lista=[]
      for i in infile:
            lista.append(i)
            print (lista[0],file=outfile)
      infile.close()
      outfile.close()
      fajl="output.py"

      filename=open(fajl,"r").read()
      compile(filename,fajl,"exec")
      print("jo kod")
except:
      print("hibás kód")



