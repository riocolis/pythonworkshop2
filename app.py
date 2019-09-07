from data import data
from menu import menu


'''
Kriteria
 1. tampilkan Nama
 2. jika ada ishidden true maka tidak ditampilkan
 3. hitung discount 
 4. tambah data baru
'''


def showData(info) :
      for i in info :
            if i['isHidden'] == False:
                  print("Name \t\t: %s"%(i['name']))
                  print("Bill \t\t: %s"%(i['Bill']))
                  print("Discount \t: %s"%(i['Discount']))
                  print("Total \t\t: %s\n"%countDiscount(i['Bill'],i['Discount']))
                   
def showDataAll(info) :
      print("----------|||||| Tax Bills |||||----------\n")
      for i in info :
            print("Name : {} , Bill : {} , Discount : {}, Total : {} ".format(i['name'],i['Bill'],i['Discount'],countDiscount(i['Bill'],i['Discount'])))

def showDataPaid(info) :
      temp1 = "---------Tax Bills -----------\n"\
            "Name : %s \n"\
            "Bill : %s \n"\
            "Discount : %s \n"\
            "Total : %s \n"
      for i in info :
            if i['isHidden'] == True:
                  print(temp1
                  %(
                        i['name'],
                        i['Bill'],
                        i['Discount'],
                        countDiscount(i['Bill'],i['Discount'])
                  ))


def countDiscount(amount, Disc):
      return amount - (amount * Disc)

def addData(newData):
      data.append(newData)

def deleteData(id):
      data.remove(data[id])
# showData(data)
#showData2(data)
#showData3(data)

if __name__ == '__main__': #mengecek apakah itu file utama atau tidak.
       while True:
            print(menu)
            inp = int(input("Masukkan pilihan  : "))
            if inp == 1 :
                  showDataAll(data)
            elif inp == 2:
                  showData(data)
            elif inp == 3:
                  showDataPaid(data)
            elif inp == 4:
                  nama = input("Masukkan Nama : ")
                  bill = int(input("Masukkan Tagihan : "))
                  discount = float(input("Masukkan Diskon : "))
                  addData({
                        'name' : nama,
                        'Bill' : bill,
                        'Discount' : discount,
                        'isHidden' : False,
                  })
            elif inp == 5:
                  index = int(input("masukkan index : "))
                  deleteData(index)
            else:
                  break 