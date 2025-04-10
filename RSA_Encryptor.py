#TryHackme Lab: RSA Encryption

#pick two primes we'll call p and q
p = #pick a prime number
q = #pick a prime number
n = p*q
phi = (p-1) * (q-1)
e = #pick a number e such that 1 < e < phi and gcd(e,phi) = 1
d = e**-1 % phi #d is the modular multiplicative inverse of e modulo phi
key = e * d % phi

public_key = (n,e)
private_key = (n,d)
print("Public key: ",public_key)
print("Private key: ",private_key) # (n, d) is the private key
