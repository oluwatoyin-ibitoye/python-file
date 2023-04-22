#!/usr/bin/env python
# coding: utf-8

# In[12]:


from cryptography.fernet import Fernet

# we will be encrypting the below string.
ReferenceID = "student@edureka"

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key

key = Fernet.generate_key()

# Instance the Fernet class with the key

fernet = Fernet(key)

# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encReferenceID = fernet.encrypt(ReferenceID.encode())

print("original string: ", ReferenceID)
print("encrypted string: ", ReferenceID)

# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decReferenceID = fernet.decrypt(encReferenceID).decode()

print("decrypted string: ", decReferenceID)


# In[ ]:




