'''ogrenciler ={
"120":{
      "Ad":"Ali",
      "Soyad":"Yılmaz",
      "Telefon":"532 000 1112"
 },
 "125":{
     "Ad":"Can",
     "Soyad":"Korkmaz",
     "Telefon":"532 000 1113"
 },
 "128":{
     "Ad":"Volkan",
     "Soyad":"Yükselen",
     "Telefon":"532 000 1114"
 }
}'''

ogrenciler={}
number = input("Ogrenci No: ")
name = input("Ogrenci Adi: ")
surname = input("Ogrenci Soyadi: ")
phone = input("Ogrenci Tel: ") 

#ogrenciler[number] = {
#    "Ad":name,
#    "Soyad":surname,
#    "Telefon":phone
#}

ogrenciler.update({
    number:{
        "Ad":name,
        "Soyad":surname,
        "Telefon":phone
    }
})


print(ogrenciler)