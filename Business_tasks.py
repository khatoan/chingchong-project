'''
Có  N nhiệm vụ được liệt kê dưới dạng 1 vòng tròn, nhiệm vụ đầu tiên kề với nhiệm vụ cuối cùng. 
Cho một số n. Bắt đầu từ nhiệm vụ đầu tiên, di chuyển theo chiều kim đồng hồ (từ thứ 1 đến thứ 2 rồi tiếp tục như vậy) và đồng thời đếm từ 1 đến n . 
Vừa di chuyển vừa đếm, khi đếm đến n, bỏ nhiệm vụ hiện tại ra khỏi danh sách và đếm từ nhiệm vụ tiếp theo. Lặp lại thủ tục này cho đến khi chỉ còn 1 nhiệm vụ. Tìm nhiệm vụ đó.
'''
def business_tasks(N,n):
    tasks = [ i for i in range(1, N+1)]
    index = 0
    while len(tasks) > 1:
        index = (index+n-1) % len(tasks)
        tasks.pop(index)
    return tasks[0]
print(business_tasks(7,3))