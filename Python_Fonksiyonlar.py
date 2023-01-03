#sinav_sonuc adında bir sözlük oluşturduk
sinav_sonuc = {
'isimler': ['Ayşe', 'Ahmet', 'Nuri', 'Nawar', 'Suzan','Ala'], 
'cinsiyet': ['K', 'E', 'E', 'E', 'K','K'], 
'vize':[80, 60, 77, 25, 36, 75],
'final' :[90, 50, 53, 100, 98, 66],
'gecme_notu':[]
}

# yeni_kayit adında fonskiyon tanımladık ve fonksiyonun işlevleri atadık
def yeni_kayit(isim,cinsiyeti,vize_notu,final_notu):
   sinav_sonuc['isimler'].append(isim)
   sinav_sonuc['cinsiyet'].append(cinsiyeti)
   sinav_sonuc['vize'].append(vize_notu)
   sinav_sonuc['final'].append(final_notu)
   
# yeni öğrenci kaydı için for döngüsü ile işlemleri tekrarladık
for i in range(2):
   
   isim_1=input('Öğrenci ismini giriniz:')
   cinsiyet_1=input("Öğrencinin cinsiyeti erkek ise E Kız ise K harfini giriniz.")
   vize_notu_1=input("Öğrencinin vizeden aldığı notu giriniz:")
   final_notu_1=input("Öğrencinin finalden aldığı notu giriniz:")

   yeni_kayit(isim_1,cinsiyet_1,vize_notu_1,final_notu_1)


# vize ve final notları dizilere aktarabilmek için boş diziler oluşturduk
vize_notlari=[]
final_notlari=[]

#oluşturduğumuz boş dizilere vize notları float olarak aktardık
for i in range(len(sinav_sonuc['isimler'])): 
   vize_notlari.append(float(sinav_sonuc['vize'][i]))
   final_notlari.append(float(sinav_sonuc['final'][i]))
  
#gecme_notu adında dizi oluşturduk ve vizenin %30 ile finalin %70 ini toplayıp bu diziye aktardık
gecme_notu = []
for i in range(len(vize_notlari)): 
   gecme_notu.append( (vize_notlari[i]*30/100) + (final_notlari[i]*70/100))

#sinav_sonuc sözlüğünde başlangıçta boş olan gecme notu yapılan işlemlerden sonra çıkan sonuçları aktardık    
sinav_sonuc['gecme_notu'].append(gecme_notu)


#liste görünümü daha düzenli görünebilmesi için her bir sözlüğü alt alta yazdırdık.
print("İsimler:",sinav_sonuc['isimler'])
print("Cinsiyetleri:",sinav_sonuc['cinsiyet'])
print("Vize Notları :",sinav_sonuc['vize'])
print("Final Notları:",sinav_sonuc['final'])
print("Geçme Notları:",sinav_sonuc['gecme_notu'])

