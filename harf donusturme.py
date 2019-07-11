# coding=utf-8
while True:
    metin=input('Bir metin yazınız.')
    if metin.isalpha()==False:  #bu metotlar yardımıyla girilen metinde sadece rakamlar için uyarı oluşturulabilir mi?
        print('Lütfen harf dışında farkı bir karakter girmeyiniz!')
    else:
        break
metin=metin.replace('i','İ').upper()
print(metin)


