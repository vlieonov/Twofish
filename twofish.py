import math
import secrets

def key_gen():
    print("Enter number of bytes for key(16, 24, 32)")
    n_bytes = int(input())
    if(n_bytes == 16 or n_bytes == 24 or n_bytes == 32):
        password = secrets.token_bytes(n_bytes)
        print(password)
        M[]
        for i in range(0, n_bytes, 4)
            
    else:
        print("Incorrect number")

key_gen()



