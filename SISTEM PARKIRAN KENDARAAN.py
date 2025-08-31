import time

# def list
datakb=[]
data_datang=[]
waktu=[]

def datang():
    x=time.time()//1
    data_datang.append(x)
    print(x)

lanjut = 0


while lanjut == 0 :

    masuk = input ("Mau masuk/keluar MALL (m/k) :  ").lower()
    
    if masuk == "m" :
    
        datang()
    
        plat = int(input("Masukan Nomor Plat : "))
        datakb.append(plat)
    
        print (" ")
        print (43*"=")
        print ("---------------PARKIRAN MALL---------------")
        print ("===========================================")
        print ("")
        print (f"     Motor dengan plat -> KB {plat} DAC   ")
        print (" ")
        print ("----------- Megamall Pontianak ------------")
        print ("------------ Jl. Ahmad Yani 1 -------------")
        print ("---------- ^_^ SELAMAT DATANG ^_^ ---------")
        print (43*"=")
    
    elif masuk == "k" :
        warning=1
        data_pulang=time.time()//1
        count=-1
        plat = int(input("Masukan Nomor Plat : "))
        for i in (datakb):
            count+=1
            if i==plat:
                warning=0
                break
            else:
                warning=1
        
        waktu=data_pulang-data_datang[count]
        print(data_datang[count])
        
        print (" ")
        print (43*"=")
        print ("---------------PARKIRAN MALL---------------")
        print ("===========================================")
        print ("")
        print (f"     Motor dengan plat -> KB {plat} DAC   ")
        print (f"----------- HARGA : Rp {100*waktu} ------------")
        print ("----------- Megamall Pontianak ------------")
        print ("------------ Jl. Ahmad Yani 1 -------------")
        print ("-- ^_^ TERIMA KASIH TELAH BERKUNJUNG ^_^ --")

        data_datang.pop(count)
        datakb.pop(count)

    elif masuk=='':
        lanjut=1