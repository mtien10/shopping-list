import jwt
from django.db import connection
from app import views
from app.views import *


class AuthenticateMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.COOKIES)
        get_access_token = request.COOKIES.get('access_token')
        print(get_access_token)
        get_refresh_token = rd.get('refresh_token')

        if get_access_token:
            response = Response()
            try:
                user = jwt.decode(get_access_token, key=settings.SECRET_KEY, algorithms=["HS256"])
                request['user_id'] = user['id']
                return user
            except Exception as e:
                if type(e) == jwt.exceptions.ExpiredSignatureError:
                    new_token = get_refresh_token.access_token
                    response.set_cookie(key='access_token', value=new_token, httponly=True)
                    request['user_id'] = user['id']
                    return user
                else:
                    raise ValueError("Not Found")
        else:
            print("Not Found")


