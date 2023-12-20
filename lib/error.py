from flask import jsonify

def error_out(message, status):
     error = {}
     error["message"] = message

     return jsonify(error), status

# EOF