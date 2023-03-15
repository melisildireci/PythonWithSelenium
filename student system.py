import sys

ogrenciList=["melis ildireci" , "hasan basri akcan", "halis ildireci" , "aylin elmalı"]
def ogrenciEkle():
    ogrenciList=["melis ildireci" , "hasan basri akcan", "halis ildireci" , "aylin elmalı"]
    
    ogrenciAdiSoyadi=input("Öğrenci adı soyadını giriniz")
    ogrenciList.append(ogrenciAdiSoyadi)
    for ogrenci in ogrenciList:
        print(ogrenci)
# bir tek öğrenci ekleme fonksiyonudur

    print(ogrenciList)

def kayitSil():
    ogrenciList=["melis ildireci" , "hasan basri akcan", "halis ildireci" , "aylin elmalı"]
    kayitSilme=input("silmek istediğin öğrenci ad soyad giriniz")
    for ogrenci in ogrenciList:
        if kayitSilme==ogrenci:
            ogrenciList.remove(kayitSilme)
            print("Kayıt silindi")
            
# bir tek öğrenci çıkarma fonksiyonudur   
            
def cokluogrenciekle():
    
    ogrenciList=["melis ildireci" , "hasan basri akcan", "halis ildireci" , "aylin elmalı"]
    ogrencisayisi= int(input("kaç öğrenci eklemek istersiniz?\n"))
    
    i=0
    if 1<= ogrencisayisi <4:
        while i < ogrencisayisi:
            ogrenciAdiSoyadi=input("Öğrenci adı soyadını giriniz\n")
            
            ogrenciList.append(ogrenciAdiSoyadi)
            print("kayit eklenedi!!!")
            i +=1
            
            print(ogrenciList)
            ogrenciNum(ogrenciList)
    else:
        sys.stderr.write("en fazla 3 ogrenci ekleyebilirsin")
        sys.stderr.flush()
    
    
# birden fazla öğrenci ekleme fonksiyonudur
def cokluKayitSil():
    ogrenciList=["melis ildireci" , "hasan basri akcan", "halis ildireci" , "aylin elmalı"]
    print(ogrenciList)
    
    kayitSilmeSayisi=int(input("Kaç öğrenci silmek istersiniz"))
    
    i =0
    if 1<= kayitSilmeSayisi <4:
        while i < kayitSilmeSayisi:
            kayitSil=input("silmek istediğin öğrenci ad soyad giriniz")
            for ogrenci in ogrenciList:
                if ogrenci==kayitSil:
                    ogrenciList.remove(ogrenci)
                    print("kayit silindi!!!")
            i +=1
            ogrenciNum(ogrenciList)
            print(ogrenciList)
    else:
        sys.stderr.write("en fazla 3 ogrenci silebilirsin!!!")
        sys.stderr.flush()
# birden fazla öğrenci çıkarma fonkisyonudur
def ogrenciNum(ogrenciList):
    
    i=0
    while i<len(ogrenciList):
        print(f"öğrenci numarası {i}" +" "+ ogrenciList[i])
        i+=1
cokluKayitSil()
#cokluogrenciekle()
#ogrenciNum(ogrenciList)