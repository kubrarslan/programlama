##1.Soru

def kar(): 
  x=int(input("Finansman geliri giriniz:"))
  y=int(input("Pazar geliri giriniz:"))
  z=int(input("Kira geliri giriniz:"))
  k=int(input("Ücret giriniz:"))
  l=int(input("Finansman gideri giriniz:"))
  m=int(input("Pazar gideri giriniz:"))
  n=int(input("Kira gideri giriniz:"))
  o=int(input("Muhasebe gideri giriniz:"))
  if(x+y+z)-(k+l+m+n+o)>1000:
    print('İşletme kar etmiştir.')
  elif(x+y+z)-(k+l+m+n+o)<1000:
    print('İşletme zarar etmiştir.')
  else:
    print('İşletme başabaş noktasındadır.')


##2.Soru

def kar():
    finGelir=int(input("finansman geliri:"))
    pzrGelir=int(input("pazar geliri:"))
    kiraGelir=int(input("kira geliri:"))
    toplamGelir=finGelir+pzrGelir+kiraGelir
    print("toplam gelir:",toplamGelir)
    ucret=int(input("ücret:"))
    finGider=int(input("finansman gideri:"))
    pzrGider=int(input("pazar gideri:"))
    kiraGider=int(input("kira gideri:"))
    mhsbGider=int(input("muhasebe gideri:"))
    toplamGider=ucret+finGider+pzrGider+kiraGider+mhsbGider
    print("toplam gider:",toplamGider)
    karZarar=toplamGelir-toplamGider
    if karZarar>1000:
        print("bu dönem kardasınız:",karZarar)
    elif karZarar<1000:
        print("bu dönem zarardasınız:",karZarar)
    else:
        print("başabaş noktası:",karZarar)
    return karZarar


##3.Soru

def abc():
    calisan=25
    stmik=int(input("satış miktarı:"))
    bsf=int(input("birim satış fiyatı:"))
    ciro=stmik*bsf
    print("döneme ait ciro:",ciro)
    adamBasiCiro=ciro/calisan
    return ("Adam Başı Ciro:",adamBasiCiro)
