from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from game.models.player.player import Player

def register(request):
    data = request.GET
    username = data.get("username", "").strip();
    password = data.get("password", "").strip();
    password_confirm = data.get("password_confirm", "").strip();

    if not username or not password:
        return JsonResponse({
            'result':"username or password cannot be empty",
        });
    if password != password_confirm:
        return JsonResponse({
            'result':"password does not match",
        });
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': "user already exists",
        })

    user = User(username=username)
    user.set_password(password)
    user.save()
    Player.objects.create(user=user, photo="https://pic1.zhimg.com/v2-9c4a0511e6ea1d3ec1e2a891ee0921a8_r.jpg")
    login(request, user);
    return JsonResponse({
        'result':"success",
    })
