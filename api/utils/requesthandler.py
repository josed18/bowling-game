from api import app
from flask import request, jsonify


def filter_error_data(data):
    if data:
        err_message = data['message']
    else:
        err_message = 'Invalid request'
    return err_message


@app.errorhandler(422)
def handle_bad_request_422(err):
    app.logger.info("ERROR: 422 " + filter_error_data(getattr(err, 'data')))
    return jsonify({
        'message': filter_error_data(getattr(err, 'data')),
    }), 422


@app.errorhandler(500)
def handle_bad_request_500(err):
    app.logger.info("ERROR: " + str(err))
    return jsonify({
        'message': "Internal error",
    }), 500


@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(403)
@app.errorhandler(405)
def handle_bad_request_404(err):
    app.logger.info("ERROR: " + str(err.description))
    return jsonify({
        'message': err.description,
    }), err.code


@app.before_request
def logger_request():
    app.logger.info(request.method + " " + request.path)


@app.before_request
def option_autoreply():
    """ Always reply 200 on OPTIONS request """
    if request.method == 'OPTIONS':
        resp = app.make_default_options_response()

        headers = None
        if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
            headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']
        h = resp.headers
        h['Access-Control-Allow-Origin'] = request.headers['Origin']
        h['Access-Control-Allow-Methods'] = request.headers['Access-Control-Request-Method']
        h['X-UA-Compatible'] = 'IE=Edge,chrome=1'
        h['Cache-Control'] = 'public, max-age=0'
        h['Content-Type'] = 'application/json'
        if headers is not None:
            h['Access-Control-Allow-Headers'] = headers
        return resp


@app.after_request
def set_allow_origin(resp):
    """ Set origin for GET, POST, PUT, DELETE requests """
    if request.method != 'OPTIONS' and 'Origin' in request.headers:
        resp.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
    resp.headers['Cache-Control'] = 'public, no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = '-1'
    resp.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    return resp
