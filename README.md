# Danh mục & lưu đồ QT – Long Giang E&C (LGEC)

Trang HTML một file, tra cứu danh mục và lưu đồ 22 quy trình (18 QT mảng thi công + 4 QT dùng lại), xây trên Base.vn.

- **Link xem (gửi khách):** https://long-giang-qt.vercel.app
- **Link dự phòng (GitHub Pages, tự cập nhật khi push):** https://anhtran-lance.github.io/long-giang-qt/
- **Repo:** https://github.com/anhtran-lance/long-giang-qt (công khai)
- **Vercel project:** `long-giang-qt` thuộc team `trananhhoai0-lang` (dashboard: https://vercel.com/trananhhoai0-lang/long-giang-qt)
- **File chính:** `index.html` – tự chứa logo, dữ liệu, giao diện; mở thẳng bằng trình duyệt là chạy, không cần build.

## Cấu trúc

```
index.html     ← BẢN MỚI NHẤT đang chạy trên web (đã có "Lưu đồ tổng quan móc nối các QT")
source/        ← mã nguồn Python dựng bản cũ (xem lưu ý bên dưới)
  HUONG-DAN-SUA.md   hướng dẫn chi tiết cú pháp dữ liệu/lưu đồ
  lgec_data.py       dữ liệu 18 QT thi công
  lg_data.py         dữ liệu 4 QT dùng lại
  lanes_map.py       đổi tên vai trò → tên đơn vị thật
  build_all.py       dựng ra index.html (bản cũ)
  assets/            logo
```

## ⚠️ Lưu ý quan trọng khi chỉnh sửa

`index.html` là bản **mới hơn** `source/`: nó có thêm lưu đồ tổng quan (`renderMap`, CSS `.map`, `.mnode`) mà `source/build_all.py` **chưa có**. Nếu chạy `build_all.py` sẽ ghi đè mất phần này.

Cách sửa an toàn:

1. **Sửa nội dung (chữ, bước, vai trò):** sửa trực tiếp `index.html`.
   - Dữ liệu nằm trong thẻ `<script id="data" type="application/json">` (JSON một dòng dài).
   - Giao diện/CSS ở đầu file; mã vẽ lưu đồ trong thẻ `<script>` cuối file.
2. **Muốn dùng lại workflow Python:** port `renderMap` + CSS `.map` từ `index.html` sang `source/build_all.py` trước, rồi mới dựng lại; so sánh bằng `diff` với `index.html`.
3. Cú pháp bước/lưu đồ: xem `source/HUONG-DAN-SUA.md` (vẫn đúng cho phần dữ liệu).

## Quy trình cập nhật & deploy

- **GitHub Pages** (link dự phòng) tự cập nhật mỗi lần push lên `main`, không dính hạn mức Vercel.
- **Vercel**: đã TẮT tự deploy khi push (đặt Ignored Build Step = `exit 0`) để tránh chạm hạn mức. Link `long-giang-qt.vercel.app` giữ nguyên bản đã deploy, KHÔNG tự đổi theo repo.
  - Muốn cập nhật link Vercel: vào Vercel → project `long-giang-qt` → Settings → Git → Ignored Build Step → chọn "Automatic", rồi push (hoặc Redeploy), xong đặt lại `exit 0`.

```bash
git clone https://github.com/anhtran-lance/long-giang-qt.git
cd long-giang-qt
# sửa index.html, mở thử bằng trình duyệt
git add -A && git commit -m "Mô tả thay đổi" && git push
```
