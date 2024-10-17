from flask import Flask, jsonify, request
from hashlib import sha256
from random import randint
from Crypto.Util.number import getPrime

# Flask app initialization
app = Flask(__name__)

# Set the parameters for Schnorr proof
p = getPrime(512)  # Large prime modulus
g = 2              # Generator
x = randint(1, p - 1)  # Private key (secret exponent)
y = pow(g, x, p)       # Public key g^x mod p

@app.route('/schnorr-proof', methods=['GET'])
def schnorr_proof():
    """
    Generate Schnorr proof for the secret exponent `x`.
    Return the proof as a JSON object.
    """
    k = randint(1, p - 1)    # Random nonce
    r = pow(g, k, p)         # Commitment
    e = int(sha256(str(r).encode()).hexdigest(), 16)  # Challenge (hash of r)
    s = (k + e * x) % (p - 1) # Response

    # Return the proof (r, e, s) to the user
    proof = {
        'r': r,
        'e': e,
        's': s,
        'y': y,  # Public key
        'g': g,  # Generator
        'p': p,  # Prime modulus
    }
    return jsonify(proof)

def verify_proof(y, r, e, s, g, p):
    """
    Verify the Schnorr proof.
    :param y: Public key
    :param r: Commitment (r)
    :param e: Challenge (e)
    :param s: Response (s)
    :param g: Generator
    :param p: Prime modulus
    :return: Boolean indicating whether the proof is valid or not
    """
    # Calculate the left-hand side (LHS) and right-hand side (RHS) of the equation
    lhs = pow(g, s, p)               # g^s mod p
    rhs = (r * pow(y, e, p)) % p     # r * y^e mod p

    return lhs == rhs  # Return True if the proof is valid

@app.route('/verify-proof', methods=['POST'])
def verify_schnorr_proof():
    """
    Verify the Schnorr proof provided by the user.
    Expects JSON with fields: 'r', 'e', 's', 'y', 'g', 'p'
    """
    data = request.get_json()

    # Extract the proof data from the request
    r = data['r']
    e = data['e']
    s = data['s']
    y = data['y']
    g = data['g']
    p = data['p']

    # Call the verification function
    is_valid = verify_proof(y, r, e, s, g, p)

    # Return the result of the verification
    result = {
        'valid': is_valid,
        'message': 'Proof is valid!' if is_valid else 'Proof is invalid!'
    }
    return jsonify(result)

@app.route('/')
def home():
    return "Schnorr Proof Server - Query /schnorr-proof to get a Schnorr proof or to verify one"

if __name__ == '__main__':
    # Start the Flask server
    app.run(host='0.0.0.0', port=5000)