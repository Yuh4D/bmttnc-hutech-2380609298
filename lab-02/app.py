from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

#route caesar cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text,key)
    return f"text: {text}<br/>key: {key} <br/>encrypted text: {encrypted_text}"

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()            
    decrypted_text = Caesar.decrypt_text(text,key)
    return f"text: {text}<br/>key: {key} <br/>decrypted text: {decrypted_text}"

                                                        
#route railfence
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.encrypt_text(text,key)
    return f"text: {text}<br/>key: {key} <br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.decrypt_text(text,key)
    return f"text: {text}<br/>key: {key} <br/>decrypted text: {decrypted_text}"

#route vigenere
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text,key)
    return f"text: {text}<br/>key: {key} <br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text,key)
    return f"text: {text}<br/>key: {key} <br/>decrypted text: {decrypted_text}"


#route playfair
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")


@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    PlayFair = PlayFairCipher()

    matrix = PlayFair.create_playfair_matrix(key)
    encrypted_text = PlayFair.playfair_encrypt(text, matrix)

    matrix_str = "<br>".join([" ".join(row) for row in matrix])

    return f"""
    Text: {text}<br/>
    Key: {key}<br/>
    <br/>
    Playfair Matrix:<br/>
    {matrix_str}<br/><br/>
    Encrypted Text: {encrypted_text}
    """


@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    PlayFair = PlayFairCipher()

    matrix = PlayFair.create_playfair_matrix(key)
    decrypted_text = PlayFair.playfair_decrypt(text, matrix)

    matrix_str = "<br>".join([" ".join(row) for row in matrix])

    return f"""
    Text: {text}<br/>
    Key: {key}<br/>
    <br/>
    Playfair Matrix:<br/>
    {matrix_str}<br/><br/>
    Decrypted Text: {decrypted_text}
    """

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)