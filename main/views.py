from django.shortcuts import render
from django.conf import settings
from main.models import Feature, Contact, About, Mission, Subtitle, Logo, Banner, Nav_logo, Footer,Team, Team2, Clint_review, Address

from django.http import HttpResponse
from django.core.mail import EmailMessage
# Create your views here.




def index(request):
    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
 
        email1 = EmailMessage(
            subject= 'from website contact',
            body= subject,
            to=('saydur776@gmail.com',),
            from_email = settings.EMAIL_HOST_USER,
            reply_to=[email],
        )

        email1.send()
        return HttpResponse("<h1>Thanks for contact us</h1>")
        

    about = About.objects.all().first()
    mission = Mission.objects.all().first()
    subtitle = Subtitle.objects.all().first()
    logo = Logo.objects.all().first()
    banner = Banner.objects.all().first()
    nav_logo = Nav_logo.objects.all().first()
    footer = Footer.objects.all().first()
    feature = Feature.objects.all()[:4]
    team = Team.objects.all()
    team2 = Team2.objects.all()
    clint_review = Clint_review.objects.all()

    address = Address.objects.all().last()

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
    'address': address,

} 

    return render(request, 'index.html',con)


