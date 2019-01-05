import sys
import math

#MODINV https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


if len(sys.argv) != 3:
    print("Erreur: arguments invalides")
    print("Les arguments du programmes sont <exposant public> <modulo>")
    sys.exit(0)
e = int(sys.argv[1])
n = int(sys.argv[2])

#ALGO https://samsclass.info/141/proj/pRSA2.htm
root = int(math.floor(math.sqrt(n)))
if root % 2 == 0:
    root = root - 1
found = False
while not found:
    if (n % root == 0):
        found = True
    else:
        root = root - 2
        
        if(root < 0):
            print("Impossible de factoriser")

p = root
q = int(n/root)

#print ("Les facteurs de n sont " + str(p) + " et " + str(q))

phin = (p-1) * (q-1)
d = modinv(e, phin)

print ("La cle privee est: " + str(d))
