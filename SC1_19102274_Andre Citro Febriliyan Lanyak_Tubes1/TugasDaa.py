# Andre Citro Febriliyan Lanyak
# 19102274
# S1IF07SC1
# Kompleksitas Algoritma Sorting
# Bubble sort dan Merge sort

#Library yang digunakan
import time #untuk menghitung runtime
from numpy.random import randint #untuk menciptakan array acak
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import ScalarFormatter

#Fungsi untuk membuat array acak
def populate(n):
    #Menggunakan fungsi randint dari library numpy.random dimana 
    #parameter pertama dan kedua adalah range nya dan parameter ketiga 
    #adalah range value yang akan di generasikan
    values = randint(0, n, n) 
    return values.tolist()

# reference: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def sortbubble(arr):
    #Deklarasi variabel n yang berisi panjang dari array
    n = len(arr)

    #Iterasi seluruh elemen dari array
    for i in range(n-1):
        #Lalui array 0 sampai n-i-1
        for j in range(0, n-i-1):
			#Tukar posisi jika elemen yang ditemukan lebih besar
			#Lalu lanjutkan ke elemen selanjutnya
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# reference: https://www.programiz.com/dsa/merge-sort  
#Deklarasi fungsi mergeSort
def mergeSort(array):
    if len(array) > 1:

        #Deklarasi varaiabel middle yang merupakan nilai median dari jumlah element dari array
        middle = len(array)//2
        
        #Deklarai subarray L(left) dan R(right) berisi data dari sebelah kiri dan kanan dari element middle 
        L = array[:middle]
        R = array[middle:]

        #Secara rekursif panggil fungsi mergeSort untuk mengurutkan array L dan R
        mergeSort(L)
        mergeSort(R)

        #Deklarasi varaiabel i, j, k
        i = j = k = 0

        #Sampai kita mencapai salah satu ujung L atau R, pilih yang lebih besar di 
        #antara elemen L dan R dan tempatkan mereka di posisi yang benar di A[p..r]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Saat kita kehabisan elemen di L atau M, ambil elemen 
        # yang tersisa dan masukkan ke A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

#Deklarasi Fungis untuk membuat grafik
def plotGraph(bubbleTime, mergeTime, arrLen):
    plt.figure(figsize=(10,6))
    print("Runtime Bubble Sort : ", end="")
    print(bubbleTime)
    print("Runtime Merge Sort : ", end="")
    print(mergeTime)
    print(arrLen)
    plt.xlabel("Nilai N")
    plt.ylabel("Runtime in second")
    plt.title("Runtime Bubble and Merge Sort")
    plt.plot(arrLen, bubbleTime, label = "Runtime Bubble Sort")
    plt.plot(arrLen, mergeTime, label = "Runtime Merge Sort")
    plt.yscale("log")
    plt.xscale("log")
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.5g'))
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.5g'))
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()

#Deklarasi Fungsi untuk membuat file.txt
def writeTxt(lists):
    for count, list in enumerate(lists):
        fileName = "file{}.txt".format(count)
        with open(fileName, 'w') as f:
            f.write(str(list))

#Fungsi main
if __name__ == '__main__':
    #Deklarasi list kosong untuk menampung data-data yang akan digunakan
    bubbleTotalRuntime = []
    mergeTotalRuntime = []
    nArr = []
    dataArr = []

    #Deklarasi perulagan while untuk menerima masukan user berupa jumlah element untuk mempopulasi list acak
    status = True
    while status == True:
        # Populasi kan array dengan 1000 angka random
        n = input("Masukan nilai n (untuk berhenti masukkan N): ")
        if n == "N":
            status = False
            break

        nArr.append(int(n))
        arr = populate(int(n))
        dataArr.append(arr)

        #Deklarasi arrLen berisi panjang dari list arr
        arrLen = len(arr)

        #Copy list arr ke varabel bubbleArr dan mergerArr
        bubbleArr = arr.copy()
        mergerArr = arr.copy()

        #Panggil Bubble dan Merge sort dan hitung runtime nya.
        bStart = time.time()
        sortbubble(bubbleArr)
        bEnd = time.time()

        mStart = time.time()
        mergeSort(mergerArr)
        mEnd = time.time()

        #Hitung Runtime nya
        bubbleTime = bEnd - bStart
        mergeTime = mEnd - mStart

        #Append hasil runtime ke dalam list
        bubbleTotalRuntime.append(bubbleTime)
        mergeTotalRuntime.append(mergeTime)

        print(f"Runtime of the Bubble sort is {bubbleTime}")
        print(f"Runtime of the Merge sort is {mergeTime}\n")

    print(bubbleTotalRuntime, mergeTotalRuntime)

    #Plot grafik untuk membandingkan runtime nya
    plotGraph(bubbleTotalRuntime, mergeTotalRuntime, nArr)
    #Panggil Fungis wirteTxt untuk menyimpan array acak yang digunakan 
    writeTxt(dataArr)

    #print ("\nBubble Sorted array is:")
    #for i in range(len(arr)):
    #    print("%d" % bubbleArr[i],end=" ")

    #print("\n\nMerge Sorted array is")
    #for i in range(len(arr)):
    #    print("%d" % mergerArr[i],end=" ")

    #if bubbleArr == mergerArr:
    #    print("\n\nbenar")

    #print(arr)