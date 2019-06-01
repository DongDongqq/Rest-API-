from  rest_framework.views import APIView, Response

from blog.serializer import *


class LoginView(APIView):

    def get(self, request):
        print('1')
        return Response({'result': '1', 'data':{"name":'1111'} , 'message': '登录成功'})

