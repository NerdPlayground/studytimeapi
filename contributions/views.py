from rooms.models import Room
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from contributions.models import Contribution
from rest_framework.generics import GenericAPIView
from contributions.serializers import ContributionSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class AddContributionAPIView(GenericAPIView):
    serializer_class= ContributionSerializer
    permission_classes= [IsAuthenticated]

    def post(self,request):
        serializer= ContributionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(contributor=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MemberContributionsAPIView(GenericAPIView):
    serializer_class= ContributionSerializer
    permission_classes= [IsAuthenticated]

    def get(self,request):
        contributions= Contribution.objects.filter(contributor=request.user)
        serializer= ContributionSerializer(contributions,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class RoomContributionsAPIView(GenericAPIView):
    serializer_class= ContributionSerializer

    def get_object(self,pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise Http404

    def get(self,request):
        room= self.get_object(pk=request.data.get('room'))
        contributions= Contribution.objects.filter(room=room)
        serializer= ContributionSerializer(contributions,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ContributionDetailAPIView(GenericAPIView):
    serializer_class= ContributionSerializer
    permission_classes= [IsAuthenticated]

    def get_object(self,pk):
        try:
            return Contribution.objects.get(pk=pk)
        except Contribution.DoesNotExist:
            raise Http404

    def put(self,request,pk):
        contribution= self.get_object(pk=pk)
        if contribution.contributor == request.user:
            serializer= ContributionSerializer(contribution,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"message":"Current user and contributor don't match"},
                status=status.HTTP_401_UNAUTHORIZED
            )

    def delete(self,request,pk):
        contribution= self.get_object(pk=pk)
        if contribution.contributor == request.user:
            contribution.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"message":"Current user and contributor don't match"},
                status=status.HTTP_401_UNAUTHORIZED
            )