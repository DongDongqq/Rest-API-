from rest_framework.views import APIView, Response
from blog.models import *
from blog.serializer import *


class RegisterView(APIView):
    def post(self, requset):
        name = requset.data.get("name")
        pwd = requset.data.get("pwd")
        print(name)

        if name and pwd:
            user = User.objects.create(name=name, pwd=pwd)
            print(user)
            sz  = RegistSerializer(user)
            return Response({"result" : '1', 'data':sz.data, 'message' : '注册成功'})
        return Response({'result' : '1', "message" : "注册失败"})