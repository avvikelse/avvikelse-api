# -*- coding: UTF-8 -*-

from bottle import request, json_dumps, response

def makeJSONP(callback, data):
    """ wraps the data in callback to prep it for JSONP response

        borrowed/stolen from https://github.com/foxbunny/HTTPy-RPC/blob/master/app.py
    """
    response_data = callback
    response_data += '('
    response_data += json_dumps(data)
    response_data += ');'
    return response_data

def auto_jsonp(f):
    """ Automatically convert JSON response to JSONP

        borrowed/stolen from https://github.com/foxbunny/HTTPy-RPC/blob/master/app.py
    """
    def new(*arg, **kw):
        callback = request.GET.get('callback')
        result_data = f(*arg, **kw)
        if callback and isinstance(result_data, dict):
            # We only do JSONP for dicts
            response.headers['Content-type'] = 'text/javascript'
            return makeJSONP(callback, result_data)
        # otherwise, we just return as usual
        return result_data

    return new