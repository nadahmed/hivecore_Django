from django.shortcuts import render
from main.models import Feature, Contact, About, Mission, Subtitle, Logo, Banner, Nav_logo, Footer,Team, Team2, Clint_review

# Create your views here.



def index(request):

    about = About.objects.all().first()
    mission = Mission.objects.all().first()
    subtitle = Subtitle.objects.all().first()
    logo = Logo.objects.all().first()
    banner = Banner.objects.all().first()
    nav_logo = Nav_logo.objects.all().first()
    footer = Footer.objects.all().first()
    feature = Feature.objects.all()
    team = Team.objects.all()
    team2 = Team2.objects.all()
    clint_review = Clint_review.objects.all()

    con = {
    'subtitle': subtitle.subtitle,
    'about': about,
    'moto': mission.moto,
    'logo':logo,
    'banner':banner,
    'nav_logo':nav_logo,
    'footer':footer,
    'feature':feature,
    'team':team,
    'team2':team2,
    'clint_review':clint_review,

}

    if request.method=="post":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        values = Contact(name=name, email=email, subject=subject)
        values.save()

    

    return render(request, 'index.html',con)


