# coding=utf-8
veri=input('Bir veri giriniz.') #Kullanıcıdan veri girisi istendi
while True:
    if not veri:  # bos giris uyarısı
        print('Bu kısımı boş bırakmayınız.')
    else:
        rakam='1234567890' #rakamlar degiskeni tanımlandı
        top=0  #rakamlar toplamı icin degisken
        kontrol=0 #rakam girisi olup olmadıgını kontrol degiskeni
        for i in veri:
            if i in rakam: #veride rakam var mı
                i=int(i)   #rakam str'yi int donusturdu
                top+=i     #rakamları birikimli topladı
                kontrol=1  #rakam girisi varasa kontrol=1
    if kontrol==0: #rakam girisi olmadıysa kontrol=0
        print('Girdiğiniz veride rakam bulunmamaktadır.')
    else: #rakam girisi varsa kontrol=1 ve top rakamlar elde edilir
        print('Giridiğiniz verideki rakamların toplamı = ', top)
    break

