with open('takımlar.txt','r') as futbolcu: #dosya okuma modunda acıldı
    isim=futbolcu.read() #dosya verileri degiskene atandı
    isim =isim.replace('ı', 'i').replace('İ','I').replace('ş','s').replace('Ş','S') #replace ile turkce
    isim =isim.replace('ğ', 'g').replace('Ğ','G').replace('ü','u').replace('Ü','U') #karakterler
    isim =isim.replace('ö', 'o').replace('Ö','O').replace('ç','c').replace('Ç','C') #degistirildi
with open('Turkce karakter off.txt','a+') as yeniListe: #yeni dosya okuma-yazma modunda acıldı
    yeniListe.write(isim) #veriler dosyaya yazıldı
