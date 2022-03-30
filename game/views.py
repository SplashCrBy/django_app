from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align:center">War of Caster</h1>'
    line2 = '<img src="https://img1.gamersky.com/image2019/02/20190228_syj_380_14/gamersky_01origin_01_201922815333FE.jpg"></img>'
    return HttpResponse(line1+line2)
