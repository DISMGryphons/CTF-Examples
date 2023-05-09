from flask import Flask
app = Flask(__name__)


@app.route('/')
def return_index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)


"""
Stick to using Flask for web challenges that require hosting.
If you're more comfortable using other frameworks, dm me at @gatari#9922.
"""