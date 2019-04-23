from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music
from .serializers import MusicSerializer

# Create your views here.

# Response 를 통해 Serializer 를 반환
# Serializer - 특정한 딕셔너리 혹은 쿼리셋 등의 파이썬 형식 데이터 타입을
# 반환하도록 해주는 아이

# music 은 쿼리셋, 일종의 리스트인데 우리가 응답하려고 하는 것은 json
# MusicSerializer가 해 주는 것은 리스트를 하나하나 json타입으로 바꿔주는 고마운 도구이다.
# 그리고 응답하는 함수는 Response 이다.
# 결과로 보내줄 데이터는 .data로 가져온다.


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()    
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
    
        