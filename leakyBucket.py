
storage = 0;   
no_of_queries = int(input("Enter the number of queries : "))
bucket_size = 	int(input("Enter the bucket size : "))
output_pkt_size = int(input("Enter the constant output packet size : "))
if output_pkt_size>bucket_size:
  print("Constant output is not possible, output packet size should be greater than bucket size")
  quit()
for i in range(0,no_of_queries):
  input_pkt_size = int(input("Enter input packet size : "))
  size_left = bucket_size - storage;
  if(input_pkt_size <= size_left):
    storage += input_pkt_size
    print("Buffer size", storage,"occupied out of bucket size", bucket_size)
  else:
    print("Packet loss = ", (input_pkt_size-(size_left)))    
    storage=bucket_size;
    print("Buffer size", storage,"occupied out of bucket size", bucket_size)                    
  if storage>=output_pkt_size:
    storage -= output_pkt_size


