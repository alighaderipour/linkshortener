from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Link
from .serializers import LinkSerializer, LinkSerializer2

@api_view(['GET'])
def get_links(request):
    links = Link.objects.all()
    serializer = LinkSerializer(links, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_employee(request):
    serializer = LinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def track_click(request, slug):
    try:
        link = Link.objects.get(slug=slug)
        link.click()  # Calls your model method
        return JsonResponse({'success': True})
    except Link.DoesNotExist:
        raise Http404("Link not found")


@api_view(['POST'])
def create_link(request):
    serializer = LinkSerializer2(data=request.data)
    if serializer.is_valid():
        serializer.save()  #‌ save اجرا می‌کنه متد save مدل و self.slug اتوماتیک پر می‌شه
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
