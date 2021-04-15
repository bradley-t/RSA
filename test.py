import sys
from rsa import *

def printProgressBar(i,max,postText):
    n_bar = 60 #size of progress bar
    j= i/max
    sys.stdout.write('\r')
    sys.stdout.write(f"[{'=' * int(n_bar * j):{n_bar}s}] {(100 * j):.2f}%  {postText}")
    sys.stdout.flush()

if __name__ == "__main__":
  sys.setrecursionlimit(10 ** 6)

  rsa_to_test = RSA()
  print("--- Testing RSA for all values of m < N ---\n")
  for m in range(rsa_to_test.n):
    printProgressBar(m, rsa_to_test.n, '')
    ct = rsa_to_test.encrypt(m)
    assert(m == rsa_to_test.decrypt(ct))
  print("All Tests Passed\n")