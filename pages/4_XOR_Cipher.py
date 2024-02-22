import streamlit as st
def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key, printing bits involved."""

    ciphertext = bytearray()
    for i in range(len(plaintext)):
        plaintext_byte = plaintext[i]
        key_byte = key[i % len(key)]
        
        # st.write bits before XOR
        
        # Perform XOR and st.write result
        xor_result = plaintext_byte ^ key_byte
        st.write(f"Plaintext byte:", format(plaintext_byte, '08b'), "=", chr(plaintext_byte))
        st.write(f"Key byte:      ", format(key_byte, '08b'), "=", chr(key_byte))
        st.write(f"XOR result:    ", format(xor_result, '08b'), "=", chr(xor_result))
        st.write("--------------------")
        ciphertext.append(xor_result)
    
    return ciphertext

def xor_decrypt(ciphertext, key):
    """Decrypts ciphertext using XOR cipher with the given key."""
    return xor_encrypt(ciphertext, key)   # XOR decryption is the same as encryption

# Example usage:
plaintext = bytes(st.text_area("Plaintext:").encode())
key = bytes(st.text_area("Key:").encode())

if st.button("Encrypt!"):
    if plaintext == key:
        st.write("Plaintext should not be equal to the key")
    elif len(plaintext.decode()) < len(key.decode()):
        st.write("Plaintext length should be equal or greater than the length of key")
    else:
        encrypted = xor_encrypt(plaintext, key)
        st.write('Ciphertext:', encrypted.decode())
        
        decrypted = xor_decrypt(encrypted, key)
        st.write('Decrypted:', decrypted.decode())