# Product Labeler Application

## Overview

Product Labeler Application là ứng dụng GUI viết bằng Python dùng để gán nhãn (label) cho hình ảnh sản phẩm với các thông tin quan trọng như tên sản phẩm, thông tin nhà sản xuất, thông tin người nhập khẩu, ngày sản xuất, ngày hết hạn và loại sản phẩm. Ứng dụng cho phép người dùng:

- Tải ảnh sản phẩm (hỗ trợ PNG, JPG, JPEG, HEIC).
- Tự động gợi ý nhãn bằng AI Google Gemini dựa trên nội dung hình ảnh.
- Kiểm tra tính hợp lệ dữ liệu nhập.
- Lưu dữ liệu ảnh và thông tin vào cơ sở dữ liệu MySQL.
- Xem danh sách sản phẩm theo loại, xem chi tiết và xóa sản phẩm.
- Xuất dữ liệu ra file JSON có đánh dấu thời gian.

Ứng dụng phù hợp cho bài tập lập trình Python về thu thập dữ liệu hình ảnh, gán nhãn (ground truth), tích hợp database và xử lý lỗi.

## Công nghệ chính

- **GUI:** Tkinter
- **Database:** MySQL
- **AI Suggestion:** Google Gemini API
- **Xử lý ảnh:** Pillow (PIL)
- **Thư viện khác:** mysql-connector-python, base64, re, json, ...

## Tính năng chính

- **Tải ảnh:** Chọn và hiển thị ảnh sản phẩm (PNG, JPG, JPEG, HEIC).
- **Gợi ý AI:** Tự động điền thông tin dựa trên ảnh qua Google Gemini AI.
- **Kiểm tra dữ liệu:**
  - Số điện thoại (hỗ trợ định dạng 0123456789, +84123456789, có dấu gạch ngang hoặc khoảng trắng).
  - Ngày tháng (hỗ trợ định dạng DD-MM-YYYY, DD/MM/YYYY, DD.MM.YYYY; kiểm tra ngày hết hạn >= ngày sản xuất và không quá xa tương lai).
  - Giới hạn độ dài text và mã hóa UTF-8.
  - Loại sản phẩm giới hạn trong các danh mục có sẵn.
- **Lưu vào database:** Lưu ảnh (dưới dạng base64 và đường dẫn) và metadata vào MySQL, xử lý trùng lặp và lỗi.
- **Xem dữ liệu:** Hiển thị danh sách sản phẩm theo loại, xem chi tiết, xem ảnh và xóa sản phẩm.
- **Xuất JSON:** Xuất toàn bộ dữ liệu sang file JSON có đánh dấu thời gian.
- **Xử lý lỗi:** Bắt lỗi file, lỗi kết nối database, lỗi nhập liệu,... với thông báo thân thiện.

## Yêu cầu

- Python 3.12 trở lên
- Cài đặt các thư viện cần thiết (chạy lệnh dưới đây):

```bash
pip install tkinter mysql-connector-python pillow google-api-python-client
