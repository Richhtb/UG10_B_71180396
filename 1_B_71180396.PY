nilaiHuruf= input("Masukkan nilai huruf PrakTekKom anda: ")
print("="*15)
switcher ={
     "A" :"Rentang nilai PrakTekKom anda adalah 85-100",
     "A-" : "Rentang nilai PrakTekKom anda adalah 80-84",
     "B+" : "Rentang nilai PrakTekKom anda adalah 75-79",
     "B" : "Rentang nilai PrakTekKom anda adalah 70-74",
     "B-" : "Rentang nilai PrakTekKom anda adalah 65-69",
     "C+" : "Rentang nilai PrakTekKom anda adalah 60-64",
     "C" : "Rentang nilai PrakTekKom anda adalah 55-59",
     "D"  : "Rentang nilai PrakTekKom anda adalah 45-54",
     "E": "Rentang nilai PrakTekKom anda adalah 0-44"
}
print(switcher.get(nilaiHuruf,"Inputan anda salah atau tidak ada pada Standar Nilai"))