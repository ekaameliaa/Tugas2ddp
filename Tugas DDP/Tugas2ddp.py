import random
import string 
dataNasabah = ()
dataNasabah2 = ()
def menu():
    print("Menu: ")
    print("[1] Buka rekening\n[2] Setoran tunai\n[3] Tarik tunai\n[4] Transfer\n[5] Lihat daftar transfer\n[6] keluar")
print("* SELAMAT DATANG DI BANK NF *")
menu()
while True:
    pilihan = input('Masukan menu pilihan anda: ')
    if pilihan == '1':
        print('*** BUKA REKENING ***')
        name = input('Masukan nama anda: ')
        setoran_awal = int(input('Masukan setoran awal: '))
        file_n = open('nasabah.txt', 'a+')
        norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
        file_n.write(norek + "," + name + "," + str(setoran_awal) + '\n')
        file_n.close()
        print(norek)
        print('Pembukaan rekening dengan nomor', norek, 'atas nama', name, 'berhasil')
        print()
        menu()
    elif pilihan == '2':
        print('*** SETORAN TUNAI ***')
        no_rek = input("Masukkan nomor rekening: ")
        nominal = eval(input("Masukkan nominal yang akan disetor: "))
        if no_rek != norek :
            print('Nomor rekening tidak terdaftar. Setoran tunai gagal')
        else : 
            file_n = open('nasabah.txt', 'w')
            print('Setoran tunai sebesar ', nominal, ' ke rekening ', no_rek, ' berhasil')
            file_n.write(norek + "," + name + "," + str(setoran_awal + nominal) + '\n')
            file_n.close()
        print()
        menu()
    elif pilihan == '3' : 
        print('*** TARIK TUNAI ***')
        rek_tarik = input("Masukkan nomor rekening: ")
        nominal_tarik = eval(input("Masukkan nominal yang akan ditarik: "))
        #if no_rek and nom == norek :
            #file_n = open('nasabah.txt', 'a+')
            #print('Tarik tunai sebesar ', nom, ' dari rekening ', no_rek, ' berhasil')
            #file_n.write(norek + "," + name + "," + str(setoran_awal - nom) + '\n')
            #file_n.close()
        if rek_tarik in dataNasabah2:
            for i in dataNasabah:
                if i[0] == rek_tarik:
                    if nominal_tarik > i[2]:
                        print("Saldo tidak mencukupi. Tarik tunai gagal.")
                        break
                    else:
                        i[2] -= nominal_tarik
                        file_n = open('nasabah.txt', 'w')
                        file_n.write(norek + "," + name + "," + str(setoran_awal - nominal) + '\n')
                        file_n.close()
                        #with open('nasabah.txt', 'w') as f:
                         #   f.write(
                          #      '\n'.join(map(lambda x: ','.join(map(str, x)),  dataNasabah)))
                        #f.close()
                        print("Tarik tunai sebesar", nominal_tarik,
                              "dari rekening", rek_tarik, "berhasil.\n")
                        break
        else:
            print("Nomor rekening tidak terdaftar. Tarik tunai gagal.")