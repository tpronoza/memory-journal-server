from memoryjournalapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    uid = request.data['uid']

    user = User.objects.filter(uid=uid).first()

    if user is not None:
        data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'image': user.image,
            'email': user.email,
            'uid': user.uid,
        }
        return Response(data)
    else:
        data = {'valid': False}
        return Response(data)

@api_view(['POST'])
def register_user(request):

    user = User.objects.create(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        image=request.data['image'],
        email=request.data['email'],
        uid=request.data['uid']
    )

    data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'image': user.image,
        'email': user.email,
        'uid': user.uid,
    }
    return Response(data)
