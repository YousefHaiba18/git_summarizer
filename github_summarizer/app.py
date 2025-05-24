from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Nothing here – try POST /webhook", 200

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "This endpoint only accepts POST", 405

    # At this point it's a POST
    payload = request.get_json(silent=True)
    print("Hello GitHub, payload:", payload)
    return "Webhook received!", 200

if __name__ == '__main__':
    # host='0.0.0.0' makes it reachable by other machines (e.g. ngrok)
    # debug=True enables hot-reload and full tracebacks
    app.run(host='0.0.0.0', port=5000, debug=True)
