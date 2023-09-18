# Importing Required Packages
import random
import math

# Initializing Required Variables
k = 32
m1, m2 = 253, 256

# Function to calculate the S function
def S(x, n):
    return (x-1) // n

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

# Function to generate prime numbers
def generate_primes(k):
    global p,q
    p = random.randint(2**(k-1), 2**k - 1)
    while not is_prime(p):
        p = random.randint(2**(k-1),2**k - 1)
    q = random.randint(2**(k-1),2**k - 1)
    while not is_prime(q) or q == p:
        q = random.randint(2**(k-1),2**k - 1)
    return p,q

# Function to calculate the GCD
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Function to generate keys
def generate_keys(k):
    global n,g,lamb,mu,public_key,private_key
    p,q = generate_primes(k)
    n = p*q
    g = n+1
    while gcd(g, n**2) != 1:
        g += 1
    lamb = (p-1)*(q-1) // gcd(p-1,q-1)
    mu = pow(S(pow(g,lamb,n**2), n), -1, n)
    public_key = (n, g)
    private_key = (lamb, mu)
    return public_key, private_key

# Fucntion to encrypt a message
def encrypt(m, public_key):
    global r,c
    n, g = public_key
    r = random.randint(1, n-1)
    c = (pow(g, m, n**2)*pow(r, n, n**2)) % (n**2)
    return c

# Function to decrypt a message
def decrypt(c, private_key, public_key):
    global L_c,m
    n = public_key[0]
    lamb, mu = private_key
    L_c = S(pow(c, lamb, n**2), n)
    m = (L_c * mu) % n
    return m

# Function to add two encrypted messages
def add(c1, c2, public_key):
    n = public_key[0]
    return (c1 * c2) % (n**2)

# Function to multiply an encrypted message with a plaintext scalar
def multiply(c, k, public_key):
    n, g = public_key
    return pow(c, k, n**2)

public_key, private_key = generate_keys(k)

'''
# Funtion Call
c1 = encrypt(m1, public_key)
c2 = encrypt(m2, public_key)
msg1 = decrypt(c1, private_key, public_key)
msg2 = decrypt(c2, private_key, public_key)

#Printing Output
print('Original Message :', m1, m2)
print('Cipher Text :', c1, c2)
print('Decrypted Message :', msg1, msg2)
'''