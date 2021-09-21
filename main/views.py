from django.shortcuts import render
from main.models import Contact, About, About_image, Mission, Subtitle, Logo, Banner, Nav_logo, Footer

# Create your views here.



def index(request):

    about = About.objects.all().first()
    about_image = About_image.objects.all().first()
    mission = Mission.objects.all().first()
    subtitle = Subtitle.objects.all().first()
    logo = Logo.objects.all().first()
    banner = Banner.objects.all().first()
    nav_logo = Nav_logo.objects.all().first()
    footer = Footer.objects.all().first()


    con = {
    'subtitle': subtitle.subtitle,
    'description': about.description,
    'about_image': about_image,
    'moto': mission.moto,
    'logo':logo,
    'banner':banner,
    'nav_logo':nav_logo,
    'footer':footer,

}

    if request.method=="post":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        values = Contact(name=name, email=email, subject=subject)
        values.save()

    

    return render(request, 'index.html',con)


