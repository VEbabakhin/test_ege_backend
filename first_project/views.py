from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from first_project.models import StudentAssignment, Student, Assignment, Theory
from first_project.serializers import AssignmentSerializer, TheorySerializer


class StudentView(APIView):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        assignments = StudentAssignment.objects.filter(student=student)
        return JsonResponse(list(assignments))


class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class TheoryViewSet(ModelViewSet):
    queryset = Theory.objects.all()
    serializer_class = TheorySerializer