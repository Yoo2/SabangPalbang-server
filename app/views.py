from django.shortcuts import render_to_response, get_object_or_404
import datetime
from django.template.context_processors import csrf
from django.utils import timezone
from app.models import Room, RoomImage, User, Board, BoardImage, Comment
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app.serializers import RoomSerializer, UserSerializer, BoardSerializer, BoardDetailSerializer, CommentSerializer
from app.forms import UploadImageForm
from django.forms.models import modelformset_factory
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import logging
import json
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)

class JSONResponse(HttpResponse):
    def __init__(self, data, **Kwargs):
        content = JSONRenderer().render(data)
        Kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **Kwargs)

def index(request):
    ImageFormSet = modelformset_factory(RoomImage, form=UploadImageForm, extra=6)
    
    if request.method == "POST":
        formset = ImageFormSet(request.POST, request.FILES, queryset=RoomImage.objects.none())

        if formset.is_valid():
            room = Room (area = request.POST['area'],
                         size = request.POST['size'],
                        floor = request.POST['floor'],
                        security_deposit = request.POST['security_deposit'],
                        month_price = request.POST['month_price'],
                        management_cost = request.POST['management_cost'],
                        air_conditioner = request.POST['air_conditioner'],
                        washer = request.POST['washer'],
                        bed = request.POST['bed'],
                        fire_type = request.POST['fire_type'],
                        desk = request.POST['desk'],
                        term = request.POST['term'],
                        veranda = request.POST['veranda'],
                        kitchen = request.POST['kitchen'],
                        tv = request.POST['tv'],
                        microwave = request.POST['microwave'],
                        two_room = request.POST['two_room'],
                        hash1 = request.POST['hash1'],
                        hash2 = request.POST['hash2'],
                        hash3 = request.POST['hash3'],
                        detail = request.POST['detail'],
                        elevator = request.POST['elevator'],
                        wardrobe = request.POST['wardrobe']
                        )
            room.save()
            
            for form in formset.cleaned_data:
                if form != {}:
                    image = form['image']
                    photo = RoomImage(room=room, image=image)
                    photo.save()
    else:
        formset = ImageFormSet(queryset=RoomImage.objects.none())

    rooms = Room.objects.all().order_by('-id')
    serializer = RoomSerializer(rooms, many=True)
    c = {'formset': formset, 'rooms': serializer.data}
    c.update(csrf(request))
        
    return render_to_response('index.html', c)

def room(request):
    if request.method == "GET":
        rooms = Room.objects.all().order_by('-id')
        serializer = RoomSerializer(rooms, many=True)
        return JSONResponse({"rooms": serializer.data})

@csrf_exempt
def user(request):
    if request.method == "POST":
        if not request.body is None:
            if not User.objects.filter(user = request.POST['user']).exists() :
                user = User(user = request.POST['user'],
                            device_token = request.POST['device_token'])
                user.save()
            else :
                user = User.objects.get(user = request.POST['user'])
                if user.device_token != request.POST['device_token']:
                    User.objects.filter(user = request.POST['user']).update(
                        device_token = request.POST['device_token'])
            return JSONResponse('')
        else :
            return HttpResponse(status=400)
    else :
        return HttpResponse(status=400)

@csrf_exempt
def board_write(request):
    if request.method == "POST":
        if not request.body is None:
            if User.objects.filter(user = request.POST['user']).exists() :
                d = timezone.localtime(timezone.now())
                board = Board(user = User.objects.get(user = request.POST['user']),
                              title = request.POST['title'],
                              content = request.POST['content'],
                              cost = request.POST['cost'],
                              item = request.POST['item'],
                              date = d.strftime('%Y-%m-%d')
                              )
                board.save()

                if not request.FILES.getlist('image') is None:
                    for f in request.FILES.getlist('image'):
                        boardImage = BoardImage(board = board,
                                                image = f
                            )
                        boardImage.save()
                return JSONResponse('')
            else :
                return HttpResponse(status=400)
        else :
            return HttpResponse(status=400)
    else :
        return HttpResponse(status=400)

def board(request):
    if request.method == "GET":
        boards = Board.objects.all().order_by('-id')
        serializer = BoardSerializer(boards, many=True)
        return JSONResponse({"boards": serializer.data})

def board_detail(request, board_id):
    if request.method == "GET":
        board = Board.objects.get(id = board_id)
        serializer = BoardDetailSerializer(board)
        return JSONResponse({"board_detail": serializer.data})

@csrf_exempt
def comment(request):
    if request.method == "POST":
        if not request.body is None:
            if User.objects.filter(user = request.POST['user']).exists() :
                d = timezone.localtime(timezone.now())
                comment = Comment(board = Board.objects.get(id = request.POST['board_id']),
                                  user = User.objects.get(user = request.POST['user']),
                                  content = request.POST['content'],
                                  date = d.strftime('%Y-%m-%d %H:%M:%S')
                                  )
                comment.save()
                return JSONResponse('')
            return HttpResponse(status=400)
        else :
            return HttpResponse(status=400)
    else :
        return HttpResponse(status=400)

def delete_room(request):
    room = Room.objects.get(id=request.GET['id'])
    room.delete()

    return HttpResponseRedirect('/')

def delete_board(request, board_id):
    if request.method == "GET":
        board = Board.objects.get(id = board_id)
        board.delete()

        return JSONResponse('')
    
