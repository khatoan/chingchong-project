"""
Đề bài “Minecraft”
Bạn đang chơi Minecraft, công việc của bạn là phải xây dựng một bức tường có độ cao lớn nhất có thể.
Hiện tại, bạn đang có sẵn một bức tường có n cột, cột thứ i có chiều cao là a_i.
Hiện tại bạn có w khối, với mỗi khối bạn có thể nâng độ cao của một cột bất kỳ thêm một đơn vị.
Bạn muốn xây bức tường sao cho độ cao của cột có độ cao nhỏ nhất là lớn nhất có thể.
Hỏi độ cao đó có thể bằng bao nhiêu?

Dữ liệu:
Dòng thứ nhất chứa hai số nguyên dương n và w (1 ≤ n ≤ 2x10^5, 1 ≤ w ≤ 10^9).
Dòng thứ hai chứa n số nguyên a₁, a₂, …, aₙ (1 ≤ aᵢ ≤ 10^9).

Kết quả: Một dòng chứa một số nguyên duy nhất là kết quả bài toán.

Hạn chế
- Subtask 1 (30% số điểm): n ≤ 100, w ≤ 10^5.
- Subtask 2 (30% số điểm): n ≤ 10^3, w ≤ 10^6.
- Subtask 3 (40% số điểm): không có ràng buộc thêm.

Ví dụ
| bàn phím | màn hình |
| -------- | -------- |
| 3 9      | 4        |
| 1 1 1    |          |

"""


def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))

    def can_build(h):
        need = 0
        for height in a:
            if height < h:
                need += h - height
        return need <= w

    L = ans = min(a)
    R = L + w
    while L <= R:
        mid = (L + R) // 2
        if can_build(mid):
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    print(ans)


if __name__ == "__main__":
    main()
