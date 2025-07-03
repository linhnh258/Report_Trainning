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

