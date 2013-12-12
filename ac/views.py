from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

# Models
from ac.models import AakashCenter, Coordinator
from ac.models import Project, Mentor, TeamMember
from ac.models import Faq

# Forms
from ac.forms import ContactForm


def index(request):
    """Index page.

    Arguments:
    - `Request`:
    """
    return render_to_response('index.html')


def about(request):
    """About page.

    Arguments:
    - `Request`:
    """
    return render_to_response('about.html')


def contact(request):
    """Contact us page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)

    if request.POST:
        contactform = ContactForm(data=request.POST)
        if contactform.is_valid():
            contactform = contactform.save(commit=True)
            messages.success(request, "Thank you for your reply. We\
            will get back to you soon.")
        else:
            print contactform.errors
            messages.error(request, "One or more fields are required or not valid.")
    else:
        contactform = ContactForm()

    context_dict = {'contactform': contactform}
    return render_to_response('contact.html', context_dict, context)


def faq(request):
    """Display FAQs.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)

    faqs = Faq.objects.all()
    context_dict = {'faqs': faqs}
    return render_to_response('faqs.html', context_dict, context)


def all_ac(request):
    context = RequestContext(request)
    aakashcenters = AakashCenter.objects.all()
    coordinators = Coordinator.objects.all()

    context_dict = {'aakashcenters': aakashcenters,
                    'coordinators': coordinators}

    return render_to_response('ac/all_ac.html', context_dict, context)

def get_ac_name_list(max_results=0, starts_with=''):
    if starts_with:
        lst = AakashCenter.objects.filter(name__contains=starts_with)
    else:
        lst = AakashCenter.objects.all()

    # if max_results > 0:
    #     if len(code_list) > max_results:
    #         code_list = code_list[:max_results]

    return lst

def get_ac_id_list(max_results=0, starts_with=''):
    if starts_with:
        lst = AakashCenter.objects.filter(ac_id__contains=starts_with)
    else:
        lst = AakashCenter.objects.all()
    return lst


def get_ac_city_list(max_results=0, starts_with=''):
    if starts_with:
        lst = AakashCenter.objects.filter(city__contains=starts_with)
    else:
        lst = AakashCenter.objects.all()
    return lst


def get_ac_state_list(max_results=0, starts_with=''):
    if starts_with:
        lst = AakashCenter.objects.filter(state__contains=starts_with)
    else:
        lst = AakashCenter.objects.all()
    return lst    

def suggest_ac_id(request):
    context = RequestContext(request)
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggest_ac_id']
        print "GET: suggestion"
        print starts_with
    else:
        print "POST: suggestion"
        starts_with = request.POST['suggest_ac_id']

    ac_id_list = get_ac_id_list(10, starts_with)
    
    context_dict = {'aakashcenters': ac_id_list}

    return render_to_response('ac/ac_list.html',
                              context_dict, context)


def suggest_ac_name(request):
    context = RequestContext(request)
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggest_ac_name']
        print "GET: suggestion"
        print starts_with
    else:
        print "POST: suggestion"
        starts_with = request.POST['suggest_ac_name']

    ac_name_list = get_ac_name_list(10, starts_with)
    
    context_dict = {'aakashcenters': ac_name_list}

    return render_to_response('ac/ac_list.html',
                              context_dict, context)
    
def suggest_ac_city(request):
    context = RequestContext(request)
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggest_ac_city']
        print "GET: suggestion"
        print starts_with
    else:
        print "POST: suggestion"
        starts_with = request.POST['suggest_ac_city']

    ac_city_list = get_ac_city_list(10, starts_with)
    
    context_dict = {'aakashcenters': ac_city_list}

    return render_to_response('ac/ac_list.html',
                              context_dict, context)

def suggest_ac_state(request):
    context = RequestContext(request)
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggest_ac_state']
        print "GET: suggestion"
        print starts_with
    else:
        print "POST: suggestion"
        starts_with = request.POST['suggest_ac_state']

    ac_state_list = get_ac_state_list(10, starts_with)
    
    context_dict = {'aakashcenters': ac_state_list}

    return render_to_response('ac/ac_list.html',
                              context_dict, context)


def download_apk(project_id):
    """Download APK.
    
    Arguments:
    - `project_id`:
    """
    project = get_object_or_404(Project, id=project_id)
    file_path = project.apk
    response = HttpResponse(
        file_path,
        mimetype="application/vnd.android.package-archive")
    response['Content-Disposition'] = 'attachment; filename=%s' % project.apk

    # increment download count
    count = project.download_count + 1
    project.download_count = count
    project.save()
    
    
def ac(request, id):
    context = RequestContext(request)

    # download APK 
    if request.POST and request.POST['download']:
        project = get_object_or_404(Project, id=request.POST['download'])
        file_path = project.apk
        response = HttpResponse(
            file_path,
            mimetype="application/vnd.android.package-archive")
        response['Content-Disposition'] = 'attachment; filename=%s' % project.apk

        # increment download count
        count = project.download_count + 1
        project.download_count = count
        project.save()

        # Server apk for download
        return response
        
    aakashcenter = AakashCenter.objects.get(pk=id)
    # print id
    # print aakashcenter.ac_id
    coordinator_name = aakashcenter.coordinator
    # print coordinator_name.id
    # print coordinator_name.user_id
    coordinator = Coordinator.objects.filter(id=coordinator_name.id)
    coordinator_detail = User.objects.get(id=coordinator_name.user_id)
    # print coordinator_detail.first_name

    projects = Project.objects.filter(ac=id)
    
    context_dict = {'aakashcenter': aakashcenter,
                    'coordinator': coordinator,
                    'projects': projects}
    return render_to_response('ac/ac.html', context_dict, context)


def projects(request):
    """List all projects."""
    context = RequestContext(request)

    # download APK 
    if request.POST and request.POST['download']:
        project = get_object_or_404(Project, id=request.POST['download'])
        file_path = project.apk
        response = HttpResponse(
            file_path,
            mimetype="application/vnd.android.package-archive")
        response['Content-Disposition'] = 'attachment; filename=%s' % project.apk

        # increment download count
        count = project.download_count + 1
        project.download_count = count
        project.save()

        # Server apk for download
        return response

    projects = Project.objects.all()
    context_dict = {'projects': projects}
    return render_to_response('ac/projects.html', context_dict, context)

def iitb(request):
    """List all projects at iitb.
    IITB has RC_ID=0."""
    context = RequestContext(request)
    try:
        iitb = AakashCenter.objects.get(ac_id=0)
        coordinator = iitb.coordinator
        coordinator = Coordinator.objects.filter(id=coordinator.id)
        projects = Project.objects.filter(ac=iitb.id)
    except:
        iitb = None
        coordinator = None
        projects = None
    
    context_dict = {'iitb': iitb,
                    'coordinator': coordinator,
                    'projects': projects}
    return render_to_response('ac/iitb.html', context_dict, context)

def project(request, id):
    context = RequestContext(request)

    # download APK 
    if request.POST and request.POST['download']:
        project = get_object_or_404(Project, id=request.POST['download'])
        file_path = project.apk
        response = HttpResponse(
            file_path,
            mimetype="application/vnd.android.package-archive")
        response['Content-Disposition'] = 'attachment; filename=%s' % project.apk

        # increment download count
        count = project.download_count + 1
        project.download_count = count
        project.save()

        # server file for download.
        return response

        
    # print id
    project = Project.objects.get(pk=id)
    
    context_dict = {'project': project}
    return render_to_response('ac/project.html', context_dict, context)
