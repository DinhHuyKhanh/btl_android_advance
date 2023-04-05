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

