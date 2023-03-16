import time;

startTime = time.time();
n = int(input("Masukkan jumlah bilangan : "))  
sum=0;  
count = 1;  
while (count<=n):  
    x = int(input("Bilangan %d : "%(count)));  
    sum = sum + x;  
    count=count+1;  
average  = sum / n;  
print("Nilai rata - rata ", average)  

endTime = time.time();

executionTime = endTime - startTime
print("Waktu Eksekusi : " , executionTime);
