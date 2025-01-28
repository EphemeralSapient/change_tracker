import random
import string

from flask import Flask, jsonify

app = Flask(__name__)
words = [0,1,2,3,4,5,6]
def generate_random_words():
    random_number = random.randint(0, 10)
    if random_number > 6:
        return words
    words[random_number] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return words

@app.route('/random_words')
def random_words():
    words = generate_random_words()
    return jsonify(words)

@app.route('/')
def index():
    return """
    I suppose, there's nothing here? eh.
"""

def run_server():
    app.run(debug=True, port=1040)

if __name__ == "__main__":
    run_server()