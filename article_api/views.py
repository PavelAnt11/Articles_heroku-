from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Articles
from .serializers import ArticlesSerializer, UserSerializer
from .permissions import IsOwner, IsAuthor
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model


class ArticlesAPIList(generics.ListAPIView):
    def get_queryset(self, *args, **kwars):
        if not self.request.user.is_anonymous:
            return Articles.objects.all()
        else:
            return Articles.objects.filter(is_public=True)

    serializer_class = ArticlesSerializer


class ArticleAPICreate(generics.CreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticated, IsAuthor, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleAPIUpdate(generics.UpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwner, )


class ArticleAPIDelete(generics.DestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwner,)


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
