import time

data_datang=[]
datakb=[]
lst_tanggal=[]
count2=0
lanjut = 0
judul='PARKIRAN MALL'
space1=7
space2=space1
harga=1
space3=9
space4=space3
toko='MEGAMALL PONTIANAK'
jalan='Jl. Ahmad Yani 1'
space5=8
space6=8

while lanjut == 0 : 
    print(43*"=")
    time.sleep(0.05)
    print("DAFTAR KODE :")
    time.sleep(0.05)
    print('0. STOP PROGRAM')
    time.sleep(0.05)
    print('1. MASUK MALL')
    time.sleep(0.05)
    print('2. KELUAR MALL')
    time.sleep(0.05)
    print('3. PENGATURAN')
    print(43*"=")
    time.sleep(0.05)
    masuk = input ("MASUKKAN KODE (0/1/2/3)         :  ").lower()
    if masuk == "1" :
        waktu_datang=time.time()//1
        tanggal=time.localtime()
        data_tanggal=[]
        for i in (tanggal):
            data_tanggal.append(i)
        lst_tanggal.append(data_tanggal)
        data_datang.append(waktu_datang)
        time.sleep(0.05) 
        plat = (input("MASUKKAN NOMOR PLAT KENDARAAN   :  "))
        print (43*"=")

        datakb.append(plat)
        
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (43*"=")
        time.sleep(0.05) 
        print (f"{'-'*(15+6-space1)} {judul} {'-'*(15+6-space2)}")
        time.sleep(0.05) 
        print ("===========================================")
        time.sleep(0.05) 
        print ("")
        time.sleep(0.05) 
        print (f' KODE ANTRIAN  :   {waktu_datang}')
        time.sleep(0.05) 
        print ("")
        time.sleep(0.05) 
        print (f" PLAT NOMOR    :   {plat}    ")
        time.sleep(0.05) 
        print ("")
        time.sleep(0.05) 
        print (f' TANGGAL       :   {lst_tanggal[count2][2]} / {lst_tanggal[count2][1]} / {lst_tanggal[count2][0]}')
        time.sleep(0.05) 
        print (f' JAM           :   {lst_tanggal[count2][3]}:{lst_tanggal[count2][4]}:{lst_tanggal[count2][5]}')
        time.sleep(0.05) 
        print ("")
        time.sleep(0.05) 
        print (43*"=")
        time.sleep(0.05) 
        print (f"{'-'*(12+9-space3)} {toko} {'-'*(11+9-space4)}")
        time.sleep(0.05) 
        print (f"{'-'*(13+8-space5)} {jalan} {'-'*(12+8-space6)}")
        time.sleep(0.05) 
        print ("---------- ^_^ SELAMAT DATANG ^_^ ---------")
        
        count2=count2+1
    elif masuk == "2" :
        count=-1
        waktu_pulang=time.time()//1
        time.sleep(0.05) 
        plat = (input("MASUKKAN NOMOR PLAT KENDARAAN   :  "))
        kondisi=1
        
        for i in datakb:
            
            count+=1
            if i==plat:
                kondisi=0
                break
            else:
                kondisi=1
        if kondisi==1:
            time.sleep(0.05) 
            print('PLAT KENDARAAN TIDAK TERDAFTAR')
            
        elif kondisi==0:
            pulang=time.localtime()
            data_pulang=[]
            for i in (pulang):
                data_pulang.append(i)
            waktu=waktu_pulang-data_datang[count]
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            print (43*"=")
            time.sleep(0.05) 
            print (f"{'-'*(15+6-space1)} {judul} {'-'*(15+6-space2)}")
            time.sleep(0.05) 
            print ("===========================================")
            time.sleep(0.05) 
            print ("")
            time.sleep(0.05) 
            print (f' KODE ANTRIAN      :   {data_datang[count]}')
            time.sleep(0.05) 
            print ("")
            time.sleep(0.05) 
            print (f" PLAT NOMOR        :   {plat}   ")
            time.sleep(0.05) 
            print ("")
            time.sleep(0.05) 
            print (f' TANGGAL DATANG    :   {lst_tanggal[count][2]} / {lst_tanggal[count][1]} / {lst_tanggal[count][0]}')
            time.sleep(0.05) 
            print (f' JAM DATANG        :   {lst_tanggal[count][3]}:{lst_tanggal[count][4]}:{lst_tanggal[count][5]}')
            time.sleep(0.05) 
            print ("")
            time.sleep(0.05) 
            print (f' TANGGAL PULANG    :   {data_pulang[2]} / {data_pulang[1]} / {data_pulang[0]}')
            time.sleep(0.05) 
            print (f' JAM PULANG        :   {data_pulang[3]}:{data_pulang[4]}:{data_pulang[5]}')
            time.sleep(0.05) 
            print ("")
            time.sleep(0.05) 
            print (f' BIAYA PARKIR      :   Rp {harga*waktu}0')
            time.sleep(0.05) 
            print ("")
            time.sleep(0.05) 
            print (43*"=")
            time.sleep(0.05) 
            print (f"{'-'*(11+9-space3)} {toko} {'-'*(12+9-space4)}")
            time.sleep(0.05) 
            print (f"{'-'*(12+8-space5)} {jalan} {'-'*(13+8-space6)}")
            time.sleep(0.05) 
            print ("-- ^_^ TERIMA KASIH TELAH BERKUNJUNG ^_^ --")
            time.sleep(0.05) 
            print (43*"=")
            
            data_datang.pop(count)
            datakb.pop(count)
            lst_tanggal.pop(count)
            count2=count2-1
        else:
            ()
    elif masuk=='3':
        while masuk=='3':
            print(43*"=")
            time.sleep(0.05)
            print("DAFTAR KODE :")
            time.sleep(0.05)
            print('0. KELUAR PENGATURAN')
            time.sleep(0.05)
            print('1. MENGGANTI JUDUL TIKET')
            time.sleep(0.05)
            print('2. MENGGANTI NAMA TOKO')
            time.sleep(0.05)
            print('3. MENGGANTI NAMA JALAN')
            time.sleep(0.05)
            print('4. MENGGANTI BIAYA PARKIR')
            time.sleep(0.05)
            print(43*"=")
            time.sleep(0.05)
            seting = input ("MASUKKAN KODE (0/1/2/3/4)       :  ").lower()
            if seting=='1':
                space=0
                judul1=judul
                judul=input('Masukan judul tiket             :  ')
                for i in judul:
                    space=space+1
                if space>39:
                    print('Maaf judul tiket tidak boleh lebih dari 39 karakter')
                    judul=judul1
                else:
                    judulganjil=space%2
                    if judulganjil==1:
                        space1=space//2+1
                        space2=space1
                    else:
                        space1=space//2+1
                        space2=space1-1
            elif seting=='4':
                harga=int(input('Masukan harga parkir/second     :  '))
            elif seting=='2':
                judul1=judul
                space=0
                judul=input('Masukan nama toko               :  ')
                for i in judul:
                    space=space+1
                if space>39:
                    print('Maaf nama toko tidak boleh lebih dari 39 karakter')
                else:
                    toko=judul
                    judulganjil=space%2
                    if judulganjil==0:
                        space3=space//2
                        space4=space3
                    else:
                        space3=space//2+1
                        space4=space3-1
                judul=judul1
            elif seting=='0':
                masuk=0
            elif seting=='3':
                judul1=judul
                space=0
                judul=input('Masukan nama jalan              :  ')
                for i in judul:
                    space=space+1
                if space>39:
                    print('Maaf nama jalan tidak boleh lebih dari 39 karakter')
                else:
                    jalan=judul
                    judulganjil=space%2
                    if judulganjil==0:
                        space5=space//2
                        space6=space5
                    else:
                        space5=space//2+1
                        space6=space5-1
                judul=judul1

    elif masuk=='0':
        lanjut=1