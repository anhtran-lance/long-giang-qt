# Hướng dẫn sửa bản HTML "Danh mục & lưu đồ QT – Long Giang E&C"

## 1. Có gì trong thư mục

```
index.html            ← file kết quả, mở thẳng bằng trình duyệt (đã gồm logo, dữ liệu, giao diện)
source/
  lgec_data.py        ← DỮ LIỆU 18 quy trình mảng thi công (sửa chủ yếu ở đây)
  lg_data.py          ← dữ liệu 4 quy trình dùng lại từ bộ trước (xem mục 4)
  lanes_map.py        ← bảng đổi tên vai trò chung chung sang tên đơn vị thật của Long Giang
  build_all.py        ← file dựng ra index.html: giao diện, CSS, mã vẽ lưu đồ
  assets/             ← logo Long Giang, Base.vn, các công ty
```

## 2. Quy trình sửa (3 bước)

1. Sửa dữ liệu trong `source/lgec_data.py` (hoặc giao diện trong `source/build_all.py`).
2. Mở Terminal, chạy:
   ```bash
   cd source
   pip3 install pillow        # chỉ lần đầu
   python3 lgec_data.py       # kiểm tra dữ liệu: phải in "18 QT OK", nếu sai sẽ báo QT nào, bước nào
   python3 build_all.py       # dựng lại ../index.html
   ```
3. Mở `index.html` để xem. Đưa lên web thì copy `index.html` lên GitHub Pages (hoặc hosting bất kỳ).

Chỉ cần Python 3 và thư viện Pillow.

## 3. Sửa nội dung một quy trình (trong `lgec_data.py`)

### 3.1 Danh sách và thứ tự: biến `SEQ`
Mỗi dòng là một quy trình:
`(mã, giai đoạn, tên quy trình, nguồn, mã danh mục Basework, nhận từ [...], chuyển sang [...], liên hệ tiến độ, ghi chú nội bộ)`
- Giai đoạn `P1`…`P5` ứng với A…E (tên giai đoạn ở biến `PHASES`).
- Số hiệu hiển thị (A1, B2, C3…) tự sinh theo thứ tự trong `SEQ`, không gõ tay.
- Nguồn: `IN_DM` = "Có trong danh mục", `ADD` = "Đề xuất bổ sung" (khung vàng đồng trên trang).
- "Nhận từ / chuyển sang" là mã QT khác (vd `["LGEC-04"]`). Mã phải tồn tại.

### 3.2 Nội dung lưu đồ: biến `NEW` (mỗi QT một khối)
```python
"LGEC-01": dict(
  goal="Mục tiêu...",  inp="Đầu vào...",  out="Đầu ra...",  app="App Base dùng...",
  lanes=["Ban Tổng giám đốc LGEC", "Phòng Đấu thầu / Dự toán", ...],   # các làn (vai trò), đánh số từ 0
  steps="""
1|4|S|Nhận thư mời thầu|2|
2|1|T|Đánh giá cơ hội|3|Phiếu đánh giá cơ hội dự thầu
3|0|D|Ban Tổng giám đốc có quyết định tham gia không?|4:Tham gia,10:Không|
"""),
```
Mỗi dòng bước có dạng: `id | số làn | loại | nội dung | bước kế tiếp | ghi chú/biểu mẫu | thời hạn`
- **số làn**: vị trí trong `lanes` (làn đầu = 0).
- **loại**: `S` bắt đầu, `T` công việc, `D` rẽ nhánh (câu hỏi), `E` kết thúc.
- **bước kế tiếp**: `5` (một nhánh), `3,4` (chạy song song), hoặc `5:Đạt,2:Chưa đạt` (nhánh có nhãn). Trỏ về bước trước thì thành mũi tên quay lại nét đứt.
- **ghi chú**: hiện ở cột "Ghi chú" trong bảng diễn giải từng bước.
- **thời hạn** (trường cuối, có thể bỏ trống): vd `3 ngày`.
- Thêm/bớt/đổi thứ tự bước: sửa dòng rồi nhớ đổi `bước kế tiếp` của các dòng trỏ tới nó. Chạy `python3 lgec_data.py` để kiểm tra trỏ sai.

### 3.3 Tên vai trò (làn)
Có thể gõ thẳng tên đơn vị thật vào `lanes`. Bảng `lanes_map.py` chỉ là cách đổi hàng loạt (vd "Phòng TCKT" → "Phòng Tài chính – Kế toán").

## 4. Bốn quy trình dùng lại dữ liệu cũ
C1 Đặt hàng VT-TB, B4 Lựa chọn NTP/NCC, C4 Quản lý chất lượng, D1 Hồ sơ thanh toán lấy nội dung từ `lg_data.py`
(khai báo ở biến `REUSE` trong `lgec_data.py`; trong `lg_data.py` tìm theo mã `QLDA-LGEC-07`, `CUNGUNG-01`, `QLDA-LGEC-02`, `QLDA-LGEC-05`).
Muốn sửa các QT này thì sửa trong khối tương ứng ở `lg_data.py` (cùng định dạng `steps` như trên), hoặc chuyển sang `NEW` rồi bỏ khỏi `REUSE`.

## 5. Sửa giao diện / chữ trên trang (`build_all.py`)
- Màu: đầu phần CSS, `--accent` (xanh navy) và `--gold` (vàng đồng).
- Câu giới thiệu, ghi chú "Bản tham khảo", ghi chú cuối trang: tìm trong hàm `renderHome()`.
- Chuỗi 7 bước tiến độ trên trang chủ: biến `spine` trong `renderHome()` (mã QT + nhãn).
- Logo: thay file trong `source/assets/` (giữ tên file).
- Cỡ khung, khoảng cách lưu đồ: hằng số `NODE_W`, `GAP`… trong phần mã vẽ lưu đồ.

## 6. Sửa nhanh ngay trên trang (không lưu)
Bấm vào chữ trong khung ở từng lưu đồ để gõ thử. Thay đổi này chỉ nằm trên trình duyệt, tải lại là mất; muốn giữ phải sửa trong `lgec_data.py` rồi dựng lại.
