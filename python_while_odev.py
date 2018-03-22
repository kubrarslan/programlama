##1.Soru

satis_miktari=500
birim_satis_fiyati=20
ciro=5000
i=0
while(ciro<=500000):
    ciro=ciro+(satis_miktari*birim_satis_fiyati)
    satis_miktari=satis_miktari+200
    birim_satis_fiyati=birim_satis_fiyati+10
    i=i+1
print('500.000 den fazla kar',i,'ayda tamamlanmıştır')



##2.Soru
stok_miktari=10000
i=0
alinan_urun=100
satilan_urun=500
fark=alinan_urun-satilan_urun
while(stok_miktari>0):
    stok_miktari=stok_miktari+fark
    i=i+1
    print(i)



##3.Soru
toplam=0
while True:
    print('Bir sayı giriniz, çıkış için 0(sıfır)')
    girilen=int(input("Sayi: "))
    if(girilen!=0):
        a=girilen%3
        toplam=toplam+a
        print('Toplam',toplam)
    else:
        print('Çıkış yapıldı')
        break



##4.Soru
calisan=50
yevmiye=90
aylik_mesai=0
haftalik_maas=630
aylik_maas=0
while aylik_mesai<=22:
    haftalik_mesai=int(input('Haftalik mesai:'))
    aylik_mesai=haftalik_mesai*4
    haftalik_maas=haftalik_maas+(haftalik_mesai*yevmiye*0.10)
    aylik_maas=aylik_maas+haftalik_maas*4
    print('Aylik maas:',aylik_maas)
else:
    print('Aylık mesai 22 saatten fazla olamaz')




##5.Soru
gunluk_uretilen=200
gunluk_defolu_urun=0
toplam_def_urun=0
i=0
while(gunluk_defolu_urun<gunluk_uretilen*0.20):
    gunluk_defolu_urun=int(input('Günlük defolu ürün miktarı:'))
    toplam_def_urun=toplam_def_urun+gunluk_defolu_urun
    i=i+1
    if(gunluk_defolu_urun>gunluk_uretilen*0.20):
        print("Defolu ürün sayısı limiti aştı")
        break
    print(i,"Günlük","Defolu Ürün Sayısı",toplam_def_urun)



        
