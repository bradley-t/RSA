# RSA Encryption/Decryption
Bradley Taylor

### Compiling and Running
The command to run a CLI for my RSA implementation is the following:
```
python3 ./main.py
```
Alternitively the implementation can be run in the python console using similar commands as the following:
```
python3 -i ./rsa.py

>>> myRSA = RSA()
>>> myRSA.p
>>> myRSA.q
>>> myRSA.n
>>> myRSA.d
>>> myRSA.encrypt(1234)
>>> myRSA.decrypt(428931)
```

### Files
The main.py file contains a CLI for my RSA implementation found in the rsa.py file. The helper functions like mod_exp and euclids are all found in util.py.

### Testing
A full test of every value between 0 and N can be run with the following command:
```
python3 ./test.py
```
The test will pretty much never finish, but I did leave it running for quite a while.