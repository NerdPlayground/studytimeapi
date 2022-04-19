from topics.models import Topic
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from topics.serializers import TopicSerializer,ViewTopicSerializer

class TopicAPIView(GenericAPIView):
    serializer_class= TopicSerializer
    permission_classes= [IsAdminUser]

    def post(self,request):
        serializer= TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TopicsAPIView(GenericAPIView):
    serializer_class= ViewTopicSerializer

    def get(self,request):
        topics= Topic.objects.all()
        serializer= ViewTopicSerializer(topics,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class TopicDetailAPIView(GenericAPIView):
    serializer_class= TopicSerializer
    permission_classes= [IsAdminUser]

    def get_object(self,pk):
        try:
            return Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            raise Http404

    def put(self,request,pk):
        topic= self.get_object(pk=pk)
        serializer= TopicSerializer(topic,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        topic= self.get_object(pk=pk)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)