RSI=int(input("Masukkan besar RSI: "))
MACD= input("Masukkan kondisi MACD: ")

if RSI >= 70 and MACD=="death-cross":
    print("RSI Lebih dari sama dengan 70 dan MACD Death-cross, saatnya Jual")
elif RSI <= 30 and MACD == "golden-cross":
    print("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya Beli")
elif RSI >= 70 and MACD == "golden-cross":
    print("RSI lebih dari sama dengan 70 dan MACD Golden-cross, Tunggu MACD sampai death-cross")
elif RSI <= 30 and MACD == "death-cross":
    print("RSI kurang dari sama dengan 30 dan MACD Death-cross, Tunggu MACD sampai Golden-cross")
elif RSI > 30 and RSI < 70:
    print("RSI berada di area 30 - 70, Bukan saatnya membelu maupun menjual")   
else:
    print("inputan anda salah")            