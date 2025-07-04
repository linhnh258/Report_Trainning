# 1. API & DOCKER 

# 2. CLOUD COMPUTING 
## 2.1. AMAZON EC2

#### Ex1: Spin up an on-demand nano EC2 instance with a storage of 10GB. Then connect to it using SSH.
![image](https://github.com/user-attachments/assets/58ceec62-1df7-4fbb-ab8e-818c1a656cb5)

#### Ex2: What is its price, region, and type?
- Type: `t2.nano`
- Region: Asia Pacific (Sydney) ap-southeast-2
- Price: $0.0073
  
  ![image](https://github.com/user-attachments/assets/9627cd9e-cd70-4ff3-a0a2-294559bdda9f)

#### Ex3: What is the difference between terminating and stopping an instance? Terminate the newly created instance.
- Stop:
  + Instance sẽ ngừng chạy, không bị tính phí cho thời gian instance chạy.
  + EBS volume vẫn được giữ lại, nên vẫn phải trả phí cho ổ cứng.
  + Có thể start lại instance bất cứ lúc nào, và mọi duwx liệu trên ổ cứng vẫn còn nguyên
- Terminate:
  + Instance và ổ cứng đi kèm bị xóa vĩnh viễn, không cần phải trả bất cứ chi phí nào tiếp theo. 
  + Không thể lấy lại được, mọi dữ liệu sẽ mất hêt.

* Terminate the newly created instance:
  
  ![image](https://github.com/user-attachments/assets/2c16e581-1371-4888-b25f-70dbe911a877)

#### Ex4: What is the difference between spot instances and on-demand instances? In which case should we choose a spot/an on-demand instance?
|| On-demand instance | Spot instance |
|---|---|---|
|Mô hình hoạt động|Trả tiền theo mức độ sử dụng (pay-as-you-go)|Sử dụng dung lượng máy chủ dư thừa của AWS. Có thể bị lấy lại bất cứ lúc nào với 2 phút cảnh báo trước|
|Chi phí|Giá cao nếu tính theo giờ, tương đối ổn định|Rất rẻ, giá biến động|
|Độ tin cậy|Cao, server không bị gián đoạn bởi AWS|Thấp, có thể bị AWS lấy lại bất cứ lúc nào|

###### Các trường hợp nên sử dụng spot/on-demand instance: 
- On-demand instance: Dùng cho các ứng dụng, tác vụ quan trọng và không thể bị gián đoạn, cho cơ sở dữ liệu hay sử dụng trong môi trường làm việc cần một server ổn định để phát triển. 
- Spot instance: Dùng khi tiết kiệm chi phí là ưu tiên hàng đầu và ứng dụng có thể chấp nhận sự gián đoạn, hoặc công việc mà dữ liệu bị mất có thể nhanh chóng được phục hồi. Ví dụ có thể sử dụng spot instance cho CI/CD pipeline.

#### Ex5: Our team wants to fine-tune an LLM. We need at least 12GB of GPU memory. Suggest an EC2 instance that we can use.
- Để đáp ứng fine-tune LLM với ít nhất 12GB GPU, cần lựa chọn một instance thuộc instance family Accelerated Computing (p, g, Ìnf, Tnr)
- Có thể lựa chọn instance **g4dn.xlarge**
  + GPU: 1x NVIDIA Tesla T4 => GPU NVIDIA được xây dựng trên kiế trúc Turing, chứa các Tensor Core, là nhân xử lý chuyên dụng cho các phép toán ma trận. Vì vậy phù hợp với mạng nơ-ron và LLM, phù hợp với việc fine-tune. 
  + Bộ nhớ GPU: 16GB => Đáp ứng yêu cầu tối thiểu là 12GB 
  + vCPU: 4 vCPU
  + RAM: 16 GiB
  + Lưu trữ cục bộ: 1 x 125 GB NVMe SSD => Phù hợp khi cần tải các tập dữ liệu lớn hoặc các checkpoints của model nhanh chóng.
  + Chi phí: 0.684 USD/hour, Chi phí vừa phải hơn một số instance cao cấp hơn ví dụ GPUA100  => hợp lý hơn cho việc fine-tune.

## 2.2. AMAZON S3
#### Ex1: Create a standard S3 bucket then upload a text file to that bucket. Send the URL to access the text file to another co-worker. Can they access it? Why/why not? If they cannot, update the configuration to change that. 
- Create a standard S3 bucket and upload file .txt

  ![image](https://github.com/user-attachments/assets/ff5141e9-484b-4fdb-b808-b8e2df916093)
  ![image](https://github.com/user-attachments/assets/d59b545c-8dbf-4cf4-a81a-6a46beaaa737)

- Người khác truy cập:

  ![image](https://github.com/user-attachments/assets/b54f0c60-97ff-429c-a7da-db31efa8343a)
  
  + Người khác không thể truy cập vào được. Do nguyên tắc "Security by Default". Để bảo vệ tài nguyên người dùng thì AWS S3 setting mọi thứ đều là riêng tư theo mặc định. Khi tạo 1 bucket mới thì AWS sẽ tự động bật "Block all public access", từ chối mọi yêu cầu bên ngoài để đảm bảo không có dữ liệu nào lộ ra. 

- Update configuration:
  + Tắt `Block all public access`
    
  ![image](https://github.com/user-attachments/assets/64981558-21b4-4dda-88bf-5e39e0c369a8)

  ![image](https://github.com/user-attachments/assets/0f552fcd-491f-4c60-bad7-a851bd0930de)

  + Edit `Bucket policy`

  ![image](https://github.com/user-attachments/assets/3827ac65-695d-4c7b-bb81-67efdb360e72)

- **Sau khi update:** Có thể truy cập xem được file 
  ![image](https://github.com/user-attachments/assets/0dbc3cbf-fbdc-4c42-9277-2264f6dece48)

#### Ex2: How much does it cost per month to store that text file on S3?
- Giá lưu trữ S3 Standard tại Region ap-southeast-2 khoảng $0.025/GB/Month
- File nặng 225 Bytes ~ 0.0000002 GB.
- Chi phí 1 tháng khoảng `0.0000002 GB * $0.025/GB ≈ $0.000000005`
  
#### Ex3: Delete the bucket you just created.
- Empyty Bucket:
  
  ![image](https://github.com/user-attachments/assets/b2674b78-fefe-4ec1-8542-96dd1d0d0b1f)

- Delete Bucket:

  ![image](https://github.com/user-attachments/assets/cd1de7a9-554d-426d-8667-411407b47b3a)

#### Ex4: On PIXTA Stock, we have over 100 million images with multiple sizes. We need to store all of them on S3. Which S3 storage class should we use?
- Lựa chọn `S3 Standard` (phù hơp cho cần truy cập nhanh, thường xuyên)
- Do S3 Standard đảm bảo mỗi bức ảnh được tải với tốc độ nhanh nhất (do Standard cung cấp độ trễ thấp ở mức mili giây), không bao gồm phí truy xuất cho mỗi lần lấy dữ liệu (Ví dụ nếu dùng Standard-IA thì khi xem một bức ảnh sẽ phải trả phí truy xuất nhỏ. Mà với hàng triệu lượt xem mỗi ngày thì phí đó sẽ cộngliệu dồn lại. Còn S3 Standard chỉ chủ yếu là phí lưu trữ, băng thông).
  
  Nếu chọn S3 Inntelligent-Tiering thì nó cần phí quản lý và giám sát cho mỗi đối tượng, khi có 100 triệu object thì chi phí đó sẽ cộng dồn và lớn hơn. Bên cạnh đó S3 Standrad-IA và S3 Glacier sẽ yêu cầu phí truy xuất như phân tích ở trước và thời gian chờ lâu hơn S3 Standard. 

## BOTO 3
#### Ex1: Install boto3 and configure access to AWS resources. 
1. Cài đặt boto3
   
   ` pip install boto3 `
2. Cấu hình quyền truy cập (Configure Access)
   - Lấy Access Key ID và Secret Access Key
   - Cài đặt AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
   - Cấu hình: Chạy lệnh `aws configure`. Lệnh này sẽ tự động tạo một thư mục `.aws` trong home và lưu các thông tin vào đó.

Boto3 đã được cài đặt để tự động tìm đến thư mục `.aws` trên để lấy các thông tin xác thực. Sau đó thì mọi script Boto3 chạy trên máy đã có quyền tương tác với tài khoản AWS. 

#### Ex2: Create start_instance.py to spin up an EC2 instance with the same configuration as section EC2
- File code tại `CloudComputing/start_instance.py`

  ![image](https://github.com/user-attachments/assets/dacd840d-bd02-4318-9662-182d42c2ead2)


#### Ex3: Create terminate_instance.py to terminate the above instance.
- File code tại `CloudComputing/terminate_instance.py`

  ![image](https://github.com/user-attachments/assets/45a79ba2-2520-4649-89a4-2f2409e5374c)


#### Ex4: Create upload_s3.py to upload any file to S3.
- File code tại `CloudComputing/upload_s3.py`

  ![image](https://github.com/user-attachments/assets/a6c2c0e5-26aa-44cb-8c64-61e24cd664b5)

