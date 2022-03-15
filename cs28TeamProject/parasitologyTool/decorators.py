from functools import wraps
from django.http import HttpResponse
from .models import *

def clinicians_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        user = UserProfile.objects.get(user=request.user)
        if user.role == 'clinician':
             return function(request, *args, **kwargs)
        else:
            return HttpResponse("you are not authorised to view this page")

  return wrap
