from django.db.models import Q, F
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import UrlSerializer
from .models import Requests, Url


class CreateUrlAPIView(CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def get_serializer_context(self):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed('your not logged in as user')
        return {'user_id': self.request.user.id}


class ListUrlAPIView(ListAPIView):
    serializer_class = UrlSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed('your not logged in as user')
        user_id = self.request.user.id
        queryset = Url.objects.filter(user_id=user_id)
        return queryset

class ListAlertAPIView(ListAPIView):
    serializer_class = UrlSerializer
    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed('your not logged in as user')
        user_id = self.request.user.id
        queryset = Url.objects.filter(user_id=user_id).filter(failed_times__gte=F('threshold'))
        return queryset


             