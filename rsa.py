from util import *

BIT_SIZE = 512
DEFAULT_E = 65537

class RSA:

  def __init__(self):
    self.p = random_large_prime(BIT_SIZE)
    self.q = random_large_prime(BIT_SIZE)
    self.phi_n = (self.p - 1) * (self.q - 1)
    self.e = DEFAULT_E

    while gcd( self.phi_n, self.e ) != 1 :
      self.p = random_large_prime( BIT_SIZE )
      self.q = random_large_prime( BIT_SIZE )
      self.phi_n = (self.p - 1) * (self.q - 1)

    self.n = self.p * self.q
    self.d = mod_inv( self.e, self.phi_n )

  def encrypt(self, m):
    return mod_exp( m, self.e, self.n )
  
  def decrypt(self, cipher_text):
    return mod_exp( cipher_text, self.d, self.n )