#Demonstrate the usage/sending of a digitally signed document. 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Get the public key
public_key = private_key.public_key()

# Message to sign
document = b"Confidential document needs to be signed"

# Sign the message
signature = private_key.sign(
    document,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Verify the signature
try:
    print("Document:", document)
    print("Signature:", signature.hex())  # print in hex for readability

    public_key.verify(
        signature,
        document,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ Signature is valid.")
except Exception as e:
    print("❌ Signature is invalid:", e)