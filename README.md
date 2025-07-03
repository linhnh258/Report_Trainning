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
