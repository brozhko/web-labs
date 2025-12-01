from flask import jsonify


def success_response(data, status_code: int = 200):
    return jsonify({"status": "success", "data": data}), status_code


def error_response(message: str, status_code: int = 400):
    return jsonify({"status": "error", "message": message}), status_code
