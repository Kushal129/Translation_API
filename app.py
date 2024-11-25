from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)  # Enable CORS
translator = Translator()
@app.route('/')
def home():
    return "Welcome"


@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        text = data.get("text")
        target_language = data.get("target_language")

        if not text or not target_language:
            return jsonify({"error": "Both 'text' and 'target_language' are required"}), 400

        translation = translator.translate(text, dest=target_language)
        return jsonify({
            "original_text": text,
            "translated_text": translation.text,
            "target_language": target_language
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=7100)
    # app.run(host='khptranslation.up.railway.app')
