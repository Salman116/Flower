from django.shortcuts import render
from app.tasks import add
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from celery.result import AsyncResult

# Create your views here.


# add.delay(10, 20)

class DefaultAPI(APIView):
    def get(self, request):
        return Response(
                {"message": "Hellow"}, status=status.HTTP_201_CREATED
            )

class DummpAPI(APIView):
    def get(self, request):
        print("sds")
        result = add.delay(10, 20)
        # print("result" , result)
        return Response(
                {"task_id": result.id}, status=status.HTTP_201_CREATED
            )

class TaskResultAPI(APIView):
    def get(self, request, task_id):
        result = AsyncResult(task_id)  # Fetch result using task ID
        return Response(
            {"task_id": task_id, "status": result.status, "result": result.result},
            status=status.HTTP_200_OK
        )