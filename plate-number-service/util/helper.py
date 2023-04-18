from functools import wraps
from typing import Any, Dict
from fastapi import Response


def wrap_responses(handler):
    @wraps(handler)
    async def middleware(*args, **kwargs) :
        # Call the controller function
        try:
            response: Response = await handler(*args, **kwargs)
            if isinstance(response, tuple):
                data, code, message = response
                dict_response: Dict[str, Any] = {
                    "data": data,
                    "code": code,
                    "message": message
                }
            else: 
                dict_response: Dict[str, Any] = {
                    "code": -1,
                    "message": message
                }

            # Return the dictionary response
            return dict_response
        except Exception as ex:
            return {
                    "code": -1,
                    "message": str(ex)
                }
    return middleware


def wrap_list_responses(handler):
    @wraps(handler)
    async def middleware(*args, **kwargs) :
        # Call the controller function
        try:
            response: Response = await handler(*args, **kwargs)
            if isinstance(response, tuple):
                total, page, page_size, data, code, msg = response
                if data is not None:
                    dict_response: Dict[str, Any] = {'data': {
                        "total": total,
                        "page": page,
                        "page_size": page_size,
                        "items": data,
                    }, "message": code, "message":msg}
                else:
                    return None, code, msg
            else: 
                dict_response: Dict[str, Any] = {
                    "code": -1,
                    "message": msg
                }

            # Return the dictionary response
            return dict_response
        except Exception as ex:
            return {
                    "code": -1,
                    "message": str(ex)
                }
    return middleware

def wrap_list_response_no_paginator(handler):
    @wraps(handler)
    async def middleware(*args, **kwargs) :
        try:
            response: Response = await handler(*args, **kwargs)
            if isinstance(response, tuple):
                data, total, code, msg = response
                if data is not None:
                    dict_response: Dict[str, Any] = {"data":{
                        "total": total,
                        "items": data,
                    }, 
                    "code": code, 
                    "message": msg}
                else:
                    dict_response: Dict[str, Any] = {
                        None, code, msg
                    }
            else:
                dict_response: Dict[str, Any] = {
                        "code": -1,
                        "message": msg
                    }

            # Return the dictionary response
            return dict_response
        except Exception as ex:
            return {
                    "code": -1,
                    "message": str(ex)
                }
    return middleware