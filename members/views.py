from members.models import Member
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from members.serializers import RegisterSerializer,EditMemberSerializer,MemberSerializer

class RegisterAPIView(GenericAPIView):
    serializer_class= RegisterSerializer

    def post(self, request):
        serializer= RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username= request.data.get('username')
            email= request.data.get('email')
            password= request.data.get('password')

            user = Member.objects.create_user(
                username= username,
                email= email,
            )
            user.set_password(password)
            user.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EditMemberAPIView(GenericAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= EditMemberSerializer

    def get_object(self,pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404
    
    def put(self,request,pk):
        if not request.user.is_staff:
            member= self.get_object(pk=pk)
            serializer= EditMemberSerializer(member,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"message":"Administrator access denied."},
                status=status.HTTP_400_BAD_REQUEST
            )

class MemberAPIView(GenericAPIView):
    serializer_class= MemberSerializer

    def get(self,request):
        member= Member.objects.get(id=request.user.id)
        serializer= MemberSerializer(member)
        return Response(serializer.data,status=status.HTTP_200_OK)

class MembersAPIView(GenericAPIView):
    permission_classes= [IsAdminUser]
    serializer_class= MemberSerializer

    def get(self,request):
        members= Member.objects.all()
        serializer= MemberSerializer(members,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class MemberDetailAPIView(GenericAPIView):
    permission_classes= [IsAdminUser]
    serializer_class= MemberSerializer

    def get_object(self,pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        member= self.get_object(pk=pk)
        serializer= MemberSerializer(member)
        return Response(serializer.data,status=status.HTTP_200_OK)