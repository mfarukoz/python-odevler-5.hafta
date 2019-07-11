# coding=utf-8
futbol_list=open('takımlar.txt','r') #verilerin okunacağı dosya okuma modunda açıldı
sesli='aeiıoöuüAEIİUÜOÖ' #sesli harfler bir değişkene atandı

for isim in futbol_list: #listeden okunan isimler satır satır isim değişkenine atandı

    if isim[0] in sesli: #isim değişkeninin ilk karakteri sesli harfler listesinde mi diye sorgulandı
        with open('İsmi sesli harfle başlayan futbolcular.txt','a+') as sesli_isim: #sesli_isim dosyası okuma ve
                                                                                    #yazma modunda açıldı
            if 'Galatasaray' in isim:
                #i=i.strip("Galatasaray")  #bu yöntem işe yaramadı! sorunu çözemedim.
                isim=isim[:-13]       # Galatasaray yazısını siliyor

            elif 'Fenerbahçe' in isim:
                isim = isim[:-12]

            elif 'Beşiktaş' in isim:
                isim = isim[:-10]

            else:
                print(i,'liste dışı')

            sesli_isim.write(isim+'\n')  #isim değişkenini sesli_isim dosyasına yazdırıyor
futbolcu_isim.close()



