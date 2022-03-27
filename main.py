import time
import random
import string

namaLaki = input("nama laki²=")
namaPerempuan = input("nama perempuan=")

if(namaLaki == namaPerempuan):
  exit("nama gak boleh sama dek")

persenJodoh = random.randint(1, 100)
print(namaLaki, "dan", namaPerempuan,"=", persenJodoh,"%")
time.sleep(2)
if(persenJodoh <= 20):
  print("status: gak jodoh lu dek")
  exit("gak jodoh skip")

if(persenJodoh <= 50):
  print("status: Friendzone")
  exit("prenjone skip")

if(persenJodoh >=50):
  print("status: saling suka")
  exit("semoga jadian dek")
if(persenJodoh ==100):
  print("status: jodoh")
  exit("√")
