## Ứng dụng Phân loại Nấm bằng Thuật toán ID3##
**Giới thiệu**

Dự án này xây dựng một ứng dụng web đơn giản bằng Flask để dự đoán xem một cây nấm ăn được hay không ăn được dựa trên 3 thuộc tính:

- Cap Shape (Hình dáng mũ nấm)

- Cap Surface (Bề mặt mũ nấm)

- Cap Color (Màu sắc mũ nấm)

## Giao diện ## 

Người dùng chọn 3 thuộc tính của nấm từ danh sách.

Ấn nút Dự đoán → Ứng dụng hiển thị kết quả:

- Nấm Ăn được

- Nấm Độc / Không ăn được

## Thuật toán sử dụng

ID3 Decision Tree (tự cài đặt, không dùng thư viện có sẵn).

Hàm đánh giá: Entropy và Information Gain.

Chỉ sử dụng 3 feature chính (cap-shape, cap-surface, cap-color) để dự đoán nhanh gọn.

## Giao diện minh họa
<img width="1783" height="646" alt="image" src="https://github.com/user-attachments/assets/967a6679-6507-481b-a067-811c2f9af8f1" />
**Nấm ăn được**
<img width="1746" height="780" alt="image" src="https://github.com/user-attachments/assets/8702f5c0-8a7c-4cca-9ac4-f11ac37e5f02" />
**Nấm không ăn được**
<img width="1761" height="757" alt="image" src="https://github.com/user-attachments/assets/1d708325-673f-484b-a22f-bcac8cbd0009" />

