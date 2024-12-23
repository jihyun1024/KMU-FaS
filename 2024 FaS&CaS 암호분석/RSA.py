import codecs

p = 0xed2f8b3524e666f29fbb524f757c4668888d2e9bb005f85e8622344564a131cf3a9756d97a3d251e45d9f87c18c679130e7cc0d54c0be78394f33ac0525d2622041f97082d21b2ca93f0fdf75c553111ae8bdbe3231b22f7524acfd72e06f4a5a38662e39ecebf5177c9e7b3ebf56c081f43a565ab5dfbff16dc647c2cf48427
q = 0xed3ade36a6ebc82da92e15dc0b045220952173a6a0a697aec0e9c37b02ab7947e28bb168a768d52845dc7a0f8ed1075fb19160ac8acd4fc5f4bd5d95f4eda13f085634b0e9420afa23f7074e9bd59f2c14d444c6c9899ecaac370fdd679931ed7e86d25c0fa92261b32a03a736807f4f42de33b1f281744bd5aaf66052d0b13b
e = 0x10001
c = 0x11c93770a75d89543f6d8e1895561489020510395e0e898982a25781ab907072e6f8b5583412cb6e1032bb942ee51cef6aa2ac34a1f48fa634efd4a0136eb6c093fef420db42c1d806eaf6032e3d7a2a1e0e608f7f526b65abdd1661d0d1e20a98874a7021b48a32c623bf62246b8ccad8283d95440520fad86985ceabb7620336cdb0aa64ab210dc350c6cdae222ea693c0a82c3deaa2a97ad82fa2df234c03ac24ce37277cff163318cff284222e989b91c82175904374acfa549ae1adb172b6e4a6cca159866c71cd47a0339d4b4bea3b52917ca0d8caf4f4899a3c135f6368c9bcb384130d38a977474e2ae5f97af64c965d8c2f4a832a90509aa9ceee1

def mod_inverse(a, m):
    g, x, y = extended_Euclidean(a, m)
    if g != 1:
        raise ValueError
    return x % m

def extended_Euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_Euclidean(b % a, a)
        return g, y - (b // a) * x, x

def decrypt(c, p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    m = pow(c, d, n)
    return m

m = decrypt(c, p, q, e)
print(codecs.decode(hex(m)[2:], 'hex').decode('utf-8'))