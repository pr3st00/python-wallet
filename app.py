from flask import Flask, request, jsonify

app = Flask(__name__)

status = {"status":"alive"}

@app.get("/health")
def health():
    return jsonify(status)

@app.get("/wallet/<id>")
def get_wallet_details(id):
        wallet = {}
        wallet["id"] = id
        return jsonify(wallet)

if __name__ == "__main__":
    app.run(debug=True)

# EOF