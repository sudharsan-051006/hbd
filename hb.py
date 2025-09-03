from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hb():
    return render_template('hb.html')  # Just the filename, no folder path

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))