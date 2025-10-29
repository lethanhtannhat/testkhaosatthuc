import csv
from datetime import datetime, timedelta
import subprocess

# Hàm hỗ trợ
def read_time_csv():
    with open("time.csv", encoding="utf-8-sig") as file:
        return list(csv.reader(file))

def write_time_csv(rows):
    with open("time.csv", "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Bắt đầu
now_utc = datetime.utcnow()
now_vn = now_utc + timedelta(hours=7)
print("time now", now_vn.strftime("%Y-%m-%d %H:%M"))

rows = read_time_csv()
remaining_rows = []
executed_count = 0
rows_to_execute = []
for i, row in enumerate(rows): # Dùng enumerate để lấy chỉ mục i
    if not row or not row[0]: continue
    try:
        # Chuyển string → datetime (giờ VN)
        scheduled_vn = datetime.strptime(row[0], "%m/%d/%Y %H:%M")

        scheduled_utc = scheduled_vn - timedelta(hours=7)

        if scheduled_utc <= now_utc:
            rows_to_execute.append((i, row)) # Lưu (index, row)
        else:
            remaining_rows.append(row)

    except Exception as e:
        print(f"Lỗi phân tích thời gian: {row} | {e}")
        remaining_rows.append(row)


for index_to_fill, row_to_run in rows_to_execute:
    print(f"its time to start: {row_to_run[0]}. Filling index: {index_to_fill}")

    try:
        # GỌI SCRIPT và BẮT BUỘC PHẢI CHỜ (check=True sẽ báo lỗi nếu script con thất bại)
        subprocess.run(
            ["python", "khaosatcheogithub.py", str(index_to_fill)],
            check=True,
            capture_output=True, # Tùy chọn, để bắt output nếu cần
            text=True
        )
        print(f"Đã điền thành công index: {index_to_fill}")
        executed_count += 1
        
        # CHỈ KHI CHẠY THÀNH CÔNG, DÒNG NÀY MỚI BỊ XÓA (KHÔNG thêm vào remaining_rows)
    
    except subprocess.CalledProcessError as e:
        print(f"Lỗi chạy khaosatcheogithub.py cho index {index_to_fill}: {e}")
        # Nếu lỗi, DÒNG NÀY KHÔNG BỊ XÓA, để thử lại lần sau.
        remaining_rows.append(row_to_run)
# Ghi lại file time.csv đã cập nhật
write_time_csv(remaining_rows)

if executed_count == 0:
    print("no time to fill")
else:
    print(f"filled {executed_count} form.")
