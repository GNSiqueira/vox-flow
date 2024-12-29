import json
from flask import Response as flaskResponse

def Response(status = 200, namedata = "", data = [], message=False):
    bory = {}
    bory[namedata] = data
    if message:
        bory['message'] = message
    return flaskResponse(json.dumps(bory), status=status, mimetype='application/json')

def ok(namedata = "", data = [], message=False):
    return Response(200, namedata, data, message)

def created(namedata = "", data = [], message=False):
    return Response(201, namedata, data, message)

def bad_request(namedata = "", data = [], message=False):
    return Response(400, namedata, data, message)

def unauthorized(namedata = "", data = [], message=False):
    return Response(401, namedata, data, message)

def forbidden(namedata = "", data = [], message=False):
    return Response(403, namedata, data, message)

def not_found(namedata = "", data = [], message=False):
    return Response(404, namedata, data, message)

def internal_server_error(namedata = "", data = [], message=False):
    return Response(500, namedata, data, message)

def conflict(namedata = "", data = [], message=False):
    return Response(409, namedata, data, message)