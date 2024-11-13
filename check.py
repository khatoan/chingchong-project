from memory_profiler import profile
import time

@profile
def Tong_while(s):
    start_time = time.perf_counter()
    T = 0
    while s > 0:
        T += s % 10
        s = s // 10 
    end_time = time.perf_counter()
    return end_time - start_time

@profile
def Tong_for(s):
    start_time = time.perf_counter()
    T = 0
    for i in str(s):
        T += int(i)
    end_time = time.perf_counter()
    return end_time - start_time

s = int("1234567890" * 100)  # Số nguyên có 1000 chữ số

time_taken1 = Tong_while(s)
print("Thời gian chạy Tong_while:", time_taken1, "giây")

time_taken = Tong_for(s)
print("Thời gian chạy Tong_for:", time_taken, "giây")


