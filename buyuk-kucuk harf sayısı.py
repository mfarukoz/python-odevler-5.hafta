# coding=utf-8
bHarf='ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ' #buyuk harfler degiskeni
kHarf=bHarf.replace('I','ı').replace('İ','i').lower() #kucuk harfler degiskeni lower ile elde edildi
rakam='1234567890' #rakamlar degiskeni
while True:
    metin=input('Bir metin giriniz.') #kullanıcı veri girisi
    if not metin: #bos giris uyarısı
        print('Hiç bir şey yazmadınız!')
    else:
        b=0 #buyuk harf sayac
        k=0 #kucuk harf sayac
        r=0 #rakam sayac
        d=0 #diger karakter sayac
        for i in metin:
            if i in bHarf:
                b+=1
            elif i in kHarf:
                k+=1
            elif i in rakam:
                r+=1
            else:
                d+=1
        break
print('Büyük harf sayısı = ',b)
print('Küçük harf sayısı = ',k)
print('Rakam sayısı = ',r)
print('Diğer  karakter sayısı = ',d)

