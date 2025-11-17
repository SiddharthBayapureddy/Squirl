# Importing custom modules
from qr_generator import qr
from url_shortener import shorten

# Flask and utilities
from flask import Flask , render_template , request,jsonify
import io
import base64

app = Flask("Squirl")


# Root endpoint
@app.route('/')
def index():
    return render_template("index.html")


# POST endpoint for shorten
@app.route('/process' , methods = ['POST'])
def process_request():

    data = request.get_json()
    original_url = data.get('url')

    action = data.get("action")

    # Check URL
    if not original_url:
        return jsonify({"ERROR" : "No URL Provided"}) , 400

    
    shortened_url = shorten(original_url)
    if not shortened_url:
        return jsonify({"error": "Invalid URL or banned domain"}), 400
    
    response_data = {
        "short_url": shortened_url,
        "type": action
    }

    # If user requested for a QR Code
    if action == "qr":
        try:
            img = qr(original_url)

            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            response_data["qr_image"] = f"data:image/png;base64,{img_str}"

        except Exception as e:
            print(f"QR Error: {e}")
            return jsonify({"error": "Failed to generate QR"}), 500


    # Or shortened url
    elif action == "shortenurl":
        pass

    return jsonify(response_data)



if __name__ == "__main__":
    app.run(debug=True, port=5000) 


