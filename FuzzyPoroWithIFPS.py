from triplesec import TripleSec
from fuzzy_extractor import FuzzyExtractor
import ipfsapi


def FuzzyPoro():

    extractor = FuzzyExtractor(10, 2)  # (CharacterLength, ErrorAllowed)
    # Sample Biometric Data
    BiometricData = input("Enter a biometric data (10 characters):")
    BiometricData = BiometricData.encode('utf-8')
    PrivateKey = input("Enter your private key:")
    PrivateKey = PrivateKey.encode('utf-8')
    # Create the key and the helper
    key, helper = extractor.generate(BiometricData)

    print ('Your key is: %s' % (key))

    # Runs your generated key through TripleSec
    KeyForTripleSec = TripleSec(key)
    EncryptedPrivateKey = KeyForTripleSec.encrypt(
        PrivateKey)  # Encrypts your private key

FuzzyPoro()
IPFS()
    # This is very insecure obviously. But this is just for testing so :/
    FileWrite = open("EncryptedKey.txt", "w+")
    FileWrite.write(str(EncryptedPrivateKey))
    FileWrite.close()

    print ('Your encrypted private key is: %s' % (EncryptedPrivateKey))

    # The second time you scan your fingerprint/biometric data
    KeyRecover = input("Enter your biometric data again:")

    KeyReturn = extractor.reproduce(
        KeyRecover, helper)  # Creates your original key

    print ('Your recovered key is: %s' % (KeyReturn))

    # Runs your regenerated key through TripleSec
    ExtractedKey = TripleSec(KeyReturn)

    try:
        print ('Your private key is: ')

        # Decodes your EncryptedPrivateKey with your regenerated encryption key
        print(ExtractedKey.decrypt(EncryptedPrivateKey).decode())
    except:
        print ('Wrong encryption key BAD BAD BAD')


def IPFS():
    try:
        api = ipfsapi.connect('127.0.0.1', 5001)
        print(api)

    except ipfsapi.exceptions.ConnectionError as ce:
        print(str(ce))

    UploadKey = api.add('EncryptedKey.txt')
    print(UploadKey)
    hash = api.cat(UploadKey['Hash'])
    print ('The content of the uploaded IPFS file is: %s' % (hash))

FuzzyPoro()
IPFS()
