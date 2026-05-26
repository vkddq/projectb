from functools import wraps
from django.http import HttpResponseForbidden

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            
            if request.user.is_authenticated and request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            
           
            return HttpResponseForbidden(
                '<h1 style="color:red; text-align:center; margin-top:50px;">403 Forbidden: You do not have permission to view this page.</h1>'
            )
        return wrapper
    return decorator