print(" __                   _                      _       ")
print("/ _\ __ _ _ __  _ __ | |__   ___  _ __   ___(_)_  __ ")
print("\ \ / _` | '_ \| '_ \| '_ \ / _ \| '_ \ / _ \ \ \/ / ")
print("_\ \ (_| | |_) | |_) | | | | (_) | | | |  __/ |>  <  ")
print("\__/\__,_| .__/| .__/|_| |_|\___/|_| |_|\___|_/_/\_\ ")
print("         |_|   |_|                                   ")
print("                                                     ")

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #alphabet adında bir liste oluşturduk

print("Decode etmek istediğiniz yazıyı yazınız : ") 

a=input()                                                                   #kullanıcıdan bir string alıp 'a' değişkenine atadık
wordlist=list(a)                                                            # 'a' değişkenini harflerine ayrıp bir 'wordlist' adında bir liste oluşturduk

sonuc=""                                                                    # 'sonuc' adında boş bir string oluşturduk

for i in range(1,len(a)):                                                   # birden başlayıp aldığımız stringin eleman sayısı kadar çalışan bir döngü oluşturduk
    
    if i%2==0:                                                              # burda frame sayımızın çift olup olmadığını kontrol ediyoruz
        continue                                                            # eğer frame sayımız çiftse bu frame'i atlıyoruz
	
    example0=wordlist[i-1] 
    example1=wordlist[i]                                                    # Sırayla harf ikililerini string olarak alıyoruz
    
    deneme=(alphabet.index(example0))
    deneme1=(alphabet.index(example1))+1                                    #harflerimizin alfabedeki index karşılığını bul 
    
    c=deneme+deneme1                                                        #sayılarımızın index numarlarını topluyoruz
    
    if c>=26: 
        b=c%26
    else :
        b=c    
    
    d=alphabet[b]                                                           # sayıların toplamlarının alfabedeki karşılığını alır    
    sonuc +=d 

print("                                                     ")    
print(sonuc)
	

                                           
                