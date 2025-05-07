mod=26
alpha={
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25,
}
beta = {
  0: "a",
  1: "b",
  2: "c",
  3: "d",
  4: "e",
  5: "f",
  6: "g",
  7: "h",
  8: "i",
  9: "j",
  10: "k",
  11: "l",
  12: "m",
  13: "n",
  14: "o",
  15: "p",
  16: "q",
  17: "r",
  18: "s",
  19: "t",
  20: "u",
  21: "v",
  22: "w",
  23: "x",
  24: "y",
  25: "z",
}

def modular_inverse(m, mod, j):
    for i in range(100):
        if m*i-mod*j >= 26:
            j+=1
        modin=m*i-mod*j #11*0-26*0=0 #11*1-26*0=11 #11*2-26*0=22 #11*3-26*0=33
    #print('modular inverse is',modin,'when i is',i)
        if modin==1:
            return i
            break
  
def daffine(min, k, p):
    for i in range(100):
        if (min*(p-k))-(26*i) <0:
            i*=-1
        affine=(min*(p-k))-(26*i)
    #print('affine is',affine,'when i is',i)
        if affine>-1 and affine <26:
            break
    return beta[affine]

def eaffine(m, k, p):
    for i in range(100):
        affine=((m*p)+k)-(26*i)
    #print('affine is',affine,'when i is',i)
        if affine>-1 and affine <26:
            break
    return beta[affine]

def affine(mod, alpha, modular_inverse, daffine, eaffine):

    m=int(input('Please enter m:'))
    k=int(input('please enter k:'))
    ch=input('Please Enter The operation you want Encryption or Decryption (e/d):').lower()
    plain=input('please enter plain phrase:').lower()

    if ch =='d':
        dec=''
        for i in range(len(plain)):
            j=0
            if plain[i]==' ':
                p=' '
                dec+=' '
            else:
                p=alpha[plain[i]]
                min=modular_inverse(m,mod,j)
                dec+=daffine(min,k,p)
        print('Your Decrypted Phrase is',dec)

    elif ch=='e':
        enc=''
        for i in range(len(plain)):
            j=0
            if plain[i]==' ':
                p=' '
                enc+=' '
            else:
                p=alpha[plain[i]]
                enc+=eaffine(m,k,p)
        print('Your Encrypted Phrase is',enc)
    else:
        print('Please Enter a valid operation')
        affine(mod, alpha,modular_inverse, daffine, eaffine)

affine(mod, alpha,modular_inverse, daffine, eaffine)
