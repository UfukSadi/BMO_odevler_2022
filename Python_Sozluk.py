sinav_sonuc = {
'isimler': ['Ayşe', 'Ahmet', 'Nuri', 'Nawar', 'Suzan','Ala'], 
'cinsiyet': ['K', 'E', 'E', 'E', 'K','K'], 
'matematik':[80, 60, 77, 25, 36, 75],
'turkce' :[90, 50, 53, 100, 98, 66]
}

kadin_sayisi = 0 # Kadınları sayısını hesaplamak için bir değişken tanımladık
erkek_sayisi = 0 # Erkeklerin sayısını hesaplamak için bir değişken tanımladık
k_mat = 0 # Kadınların almış olduğu toplam matematik notunu hesaplamak için bir değişken atadık
e_mat = 0 # Erkeklerin almış olduğu toplam matematik notunu hesaplamak için bir değişken atadık
k_tr = 0 # Kadınların almış olduğu toplam türkçe notunu hesaplamak için bir değişken atadık
e_tr = 0 # Erkeklerin almış olduğu toplam türkçe notunu hesaplamak için bir değişken atadık
k_tr_not = [] # En yüksek notu bulabilmek için boş bir dizi oluşturduk
e_tr_not = []


for i in range(len(sinav_sonuc['cinsiyet'])): # Döngü sayımızı len fonksiyonu ile hesapladık
     if  sinav_sonuc['cinsiyet'][i] == 'K': # Cinsiyet dizisindeki i elemanı K ya eşit ise aşağıdaki işlemleri yap
         kadin_sayisi +=1 # Kadın sayısını 1 arttır
         k_mat = k_mat + sinav_sonuc['matematik'][i] # Kadınların matematik notunu dizideki i elemana denk gelen notu al ve k_mat değişkenine ata önceden değer varsa toplayarak ekle
         k_tr = k_tr + sinav_sonuc['turkce'][i] # Aynı mantık ile türkçe notlarını hesapladık
         k_tr_not.append(sinav_sonuc['turkce'][i])    
        
     else: # Eğer cinsiyet dizisindeki i elemanı K ya eşit değil ise aşağıdaki işlemleri yap
         erkek_sayisi +=1 
         e_mat = e_mat + sinav_sonuc['matematik'][i] # Kadınların toplam notu hesaplama yapınca kullandığımız mantık ile aynı işlemler 
         e_tr = e_tr + sinav_sonuc['turkce'][i]
         e_tr_not.append(sinav_sonuc['turkce'][i])         


print(f"Kadınların Matematik Not Ortalaması:{k_mat/kadin_sayisi}") # k_mat değişkeni ile kadın sayısını böldük
print(f"Erkeklerin Matematik Not Ortalaması:{e_mat/erkek_sayisi}") 
print(f"Kadınların Türkçe Not Ortalaması:{k_tr/kadin_sayisi}") 
print(f"Erkeklerin Türkçe Not Ortalaması:{e_tr/erkek_sayisi}")
print(f"Sınıfın Türkçe Not Ortalaması:{(e_tr + k_tr)/(kadin_sayisi+erkek_sayisi)}") # Sınıfın türkçe not ortalaması için toplam türkçe notu / toplam kişi işlemi yaptık
print(f"Kadınlar Arasında En Yüksek Türkçe Notu:{max(k_tr_not)}") # Kadınlar arasında en yüksek notu döngüden aktardığımız diziden max fonksiyonu ile aldık.
print(f"Kadınlar Arasında En Yüksek Türkçe Notu:{max(e_tr_not)}") # Aynı mantık ile Erkekleri yazdırdık.