import hashlib



# Output: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8


string="pad"
encoded=string.encode()
result = hashlib.sha256(encoded)
print("String : ", end ="")
print(string)
print("Hash Value : ", end ="")
print(result)
print("Hexadecimal equivalent: ",result.hexdigest())
print("Digest Size : ", end ="")
print(result.digest_size)
print("Block Size : ", end ="")
print(result.block_size)



print (len(result.digest()))