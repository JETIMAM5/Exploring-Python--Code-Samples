maasAli=5000
maasMehmet=4000
vergiOrani=0.27

print(maasAli-(maasAli*vergiOrani))
print(maasMehmet-(maasMehmet*vergiOrani))

# Değişken tanımlama kuralları 
#1-Rakam ile başlayamaz 
number1 = 10
# Sadece deklare edip bırakamayız bir değer de assign etmemiz gerekir 
#_ ile de başlayabilir bi problem yok 
print(number1)
number1= 20 
print(number1)
#Bir değer assign ettikten sonra değiştirebilirsin 
number1 +=30
print(number1)
# += ile değerini arttırabiliriz değişkenin 


#Büyük - Küçük harf duyarlılığı vardır yani Number ile number aynı şeyler değiller
#Değişken atnımlaması yawparken Türkçe karakter kullanmayalım

x=1                #int
y=2.3              #float
name="Çınar"       #String
isStudent = True   #Bool


a = '10'
b = '20'
print(a+b)
#Bu gibi bi durumda string birleştirme işi yapılır çünkü bunlar string türden verilerdir 

x,y,name,isStudent= (1,2.3,"Çınar",True)
# Bu şekilde her birini tek bir satırda da tanımlayabiliriz 
