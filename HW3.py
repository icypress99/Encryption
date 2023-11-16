MAX = 1000000007

def hash(message):
    res = 1
    for c in message:
        res = res * ord(c) % MAX
    return res

def sign(message, p, q, g, private_key):
    k = 4
    r = pow(g, k, p) % q
    h = hash(message)
    s = (pow(k, -1, q) * (h + private_key * r)) % q
    return (r, s)

def verify(signature, tampered_message, p, q, g, public_key):
    r, s = signature
    w = pow(s, -1, q)
    h = hash(tampered_message)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(public_key, u2, p)) % p) % q
    return v == r

message_amirali = "salam"
message_abbas = "salam"
p = 23
q = 11
g = 16
private_key_amirali = 9
public_key_abbas = 8

x = private_key_amirali
y = pow(g, x, p)
signature = sign(message_amirali, p, q, g, private_key_amirali)
w = pow(signature[1], -1, q)
u1 = (hash(message_abbas) * w) % q
u2 = (signature[0] * w) % q
v = ((pow(g, u1, p) * pow(public_key_abbas, u2, p)) % p) % q
result = verify(signature, message_abbas, p, q, g, public_key_abbas)

print(p)
print(q)
print(g)
print(x)
print(y)
print(signature[0])
print(signature[1])
print(w)
print(u1)
print(u2)
print(v)
print(result)