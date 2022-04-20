from rooms.models import Room
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rooms.serializers import RoomSerializer,ViewRoomSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class AddRoomAPIView(GenericAPIView):
    serializer_class= RoomSerializer
    permission_classes= [IsAuthenticated]
    
    def post(self,request):
        serializer= RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(host=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AllRoomsAPIView(GenericAPIView):
    serializer_class= ViewRoomSerializer

    def get(self,request):
        rooms= Room.objects.all()
        serializer= ViewRoomSerializer(rooms,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class MemberRoomsAPIView(GenericAPIView):
    serializer_class= ViewRoomSerializer
    permission_classes= [IsAuthenticated]

    def get(self,request):
        rooms= Room.objects.filter(host=request.user)
        serializer= ViewRoomSerializer(rooms,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class IndividualRoomAPIView(GenericAPIView):
    serializer_class= ViewRoomSerializer

    def get_object(self,pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        room= self.get_object(pk=pk)
        serializer= ViewRoomSerializer(room)
        return Response(serializer.data,status=status.HTTP_200_OK)

class RoomDetailAPIView(GenericAPIView):
    serializer_class= RoomSerializer
    permission_classes= [IsAuthenticated]

    def get_object(self,pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise Http404

    def put(self,request,pk):
        room= self.get_object(pk=pk)
        if room.host == request.user:
            serializer= RoomSerializer(room,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"message":"Current user and room host don't match"},
                status=status.HTTP_401_UNAUTHORIZED
            )

    def delete(self,request,pk):
        room= self.get_object(pk=pk)
        if room.host == request.user:
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"message":"Current user and room host don't match"},
                status=status.HTTP_401_UNAUTHORIZED
            )