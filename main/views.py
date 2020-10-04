from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    with open('data.txt', 'r+') as data:
        old = float(data.read())
        new = old + 2
        data.seek(0)
        data.write(str(new))
    return Response({'trump': new, 'biden': 100 - new})



