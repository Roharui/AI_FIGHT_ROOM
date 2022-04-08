

import os
import jwt
from functools import wraps
from flask import Response, current_app, request
from requests import post


def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    access_token = request.headers.get("Authorization")
    if access_token is not None:
      try:
        payload = post(os.getenv("AUTH_HOST"), json={"token": access_token}).json()
      except Exception:
        payload = None

      if payload is None:
        return Response(status=401)
    else:
        return Response(status=401)
    
    return f(payload, *args, **kwargs)
  return decorated_function