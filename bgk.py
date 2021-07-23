import random

print("TENTUKAN PILIHANMU:")
print("1.Batu")
print("2.Gunting")
print("3.Kertas")

def gameset():
  player = int(input("Masukkan pilihanmu: "))
  comp = random.choice(["batu", "gunting", "kertas"])
  if player == 1:
    print("Kamu memilih batu")
    print("dan komputer memilih",comp)
    if comp == "batu":
      print("Maka hasilnya seri")
    if comp == "gunting":
      print("Maka hasilnya kamu menang")
    if comp == "kertas":
      print("Maka hasilnya kamu kalah")
  
  if player == 2:
    print("Kamu memilih gunting")
    print("dan komputer memilih",comp)
    if comp == "batu":
      print("Maka hasilnya kamu kalah")
    if comp == "gunting":
      print("Maka hasilnya seri")
    if comp == "kertas":
      print("Maka hasilnya kamu menang")
  
  if player == 3:
    print("Kamu memilih kertas")
    print("dan komputer memilih",comp)
    if comp == "batu":
      print("Maka hasilnya kamu menang")
    if comp == "gunting":
      print("Maka hasilnya kamu kalah")
    if comp == "kertas":
      print("Maka hasilnya seri")
      
gameset()
  