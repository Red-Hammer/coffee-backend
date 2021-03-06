from flask import jsonify, make_response


def construct_standard_response(body):
    response = jsonify(body)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


def build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
