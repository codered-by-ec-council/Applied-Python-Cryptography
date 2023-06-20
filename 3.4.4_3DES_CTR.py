from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def DES3_CTR_encrypt(plaintext, DES3_key, nonce):

    DES3_CTR_cipher = DES3.new(DES3_key, DES3.MODE_CTR, nonce=nonce)
    ciphertext = DES3_CTR_cipher.encrypt(plaintext)

    return ciphertext

def DES3_CTR_decrypt(ciphertext, DES3_key, nonce):

    # Let's create our triple DES CTR cipher variable making it equal to the DES3 module snew function
    # pass in our triple DES key, set the mdoe of operation to coutner mode, and our nonce once again
    # equal to our nonce
    DES3_CTR_cipher = DES3.new(DES3_key, DES3.MODE_CTR, nonce=nonce)

    # Next delcare our decrypted plaintext variable equal to our newly created cipher and call the
    # decrypt function, while only passing in the ciphertext, since we do not require any padding
    # nor do we require a block size
    decrypted_plaintext = DES3_CTR_cipher.decrypt(ciphertext)

    # Finally reutrn our decrypted plaintext
    return decrypted_plaintext

# There we have it, now more of the same, we want to declare our plaintext variable and have it equal
# to the input function with a message and encode it
# So let's declare that here
plaintext = input("Enter plaintext: ").encode()

# Next we want to create our triple DES key, and once again we'll be calling that built in function of the
# triple DES module called adjust key parity, passing into it our get random bytes function with 24 bytes
# as once again this will be the equivalent of three keys as we want to increase the length
DES3_key = DES3.adjust_key_parity(get_random_bytes(24))

# Like with the previous DES example, we want the nonce to be equal to the get random bytes function
# with 7 bytes being passed into it
nonce = get_random_bytes(7)

# Now, let's get our ciphertext, we'll have this equal to the triple DES ctr encrypt function and pass in
# our plaintext, our triple DES key and our nonce
ciphertext = DES3_CTR_encrypt(plaintext, DES3_key, nonce)

# Then we'll declare the decrypted plaintext variable, of course making it equal to the triple DES CTR decrypt
# function and pass in our ciphertext our triple DES key and our nonce
decrypted_plaintext = DES3_CTR_decrypt(ciphertext, DES3_key, nonce)

# Now that we've got all our variables and functions declared, let's go ahead and get our results printed out
# to the console
# We'll start with our plaintext, making sure to decode it with that default of UTF8
print ("Plaintext: ", plaintext.decode())
# Then we'll print out our ciphertext while calling that hex function for prettification
print ("Ciphertext: ", ciphertext.hex())
# And finally, our decrypted plaintext, also getting our decode function
print ("Decrypted plaintext: ", decrypted_plaintext.decode())