from rsa import *

menu = """
Select what you would like to do:

      1 - Print Key Values
      2 - Encrypt a Number
      3 - Decrypt a Number
      4 - Generate a New Key
      0 - Exit

Enter your choice:"""

def printKeyValues(myRSA):
  print("\n---RSA Keypair Values---")
  print("\nPrime number p:\n%d" % myRSA.p)
  print("\nPrime q:\n%d" % myRSA.q)
  print("\nValue for N:\n%d" % myRSA.n)
  print("\nPublic key exponent e:\n%d" % myRSA.e)
  print("\nPrivate key exponent d:\n%d" % myRSA.d)

def encryptSelected(myRSA):
  print("\n---RSA Encryption---")
  message = int(input("\nPlease input value to encrypt:\n"))
  print("\nResulting cipher value:\n%d" % myRSA.encrypt(message))

def decryptSelected(myRSA):
  print("\n---RSA Decryption---")
  cipher_text = int(input("\nPlease input value to decrypt:\n"))
  print("\nDecrypted value:\n%d" % myRSA.decrypt(cipher_text))

if __name__ == "__main__":
  myRSA = RSA()
  print('--- RSA CLI ---')
  while(True):
    try:
      selection = int(input(menu))
    except Exception:
      print("\nPlease make a valid selection\n")
      continue
    if selection == 0:
      break
    elif selection == 1:
      printKeyValues(myRSA)
    elif selection == 2:
      encryptSelected(myRSA)
    elif selection == 3:
      decryptSelected(myRSA)
    elif selection == 4:
      myRSA = RSA()
      print("\n--- New Key Generated ---\n")
    else:
      print("\nPlease make a valid selection\n")

