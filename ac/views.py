from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory

# Models
from ac.models import AakashCentre, Coordinator
from ac.models import Project, Mentor, TeamMember
from ac.models import Faq, Pub

# Forms
from ac.forms import ContactForm, AakashCentreForm
from ac.forms import CoordinatorForm, UserForm
from ac.forms import ProjectForm
from ac.forms import MemberForm, MentorForm

# Local libs
from get_list import get_ac_id_list, get_ac_city_list
from get_list import get_ac_name_list, get_ac_state_list
from get_list import get_project_list


def index(request):
    """Index page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)
    return render_to_response('index.html', context)


def about(request):
    """About page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)
    return render_to_response('about.html', context)


def compete(request):
    """Competition page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('compete.html', context)


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


def pubs(request):
    """Publications and Articles/links related to Aakash.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)

    pubs = Pub.objects.all()
    context_dict = {'pubs': pubs}
    return render_to_response('pubs.html', context_dict, context)    


def all_ac(request):
    context = RequestContext(request)
    aakashcentres = AakashCentre.objects.filter(active=True).order_by('ac_id')
    coordinators = Coordinator.objects.all()

    context_dict = {'aakashcentres': aakashcentres,
                    'coordinators': coordinators}

    return render_to_response('ac/all_ac.html', context_dict, context)


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
    
    context_dict = {'aakashcentres': ac_id_list}

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
    
    context_dict = {'aakashcentres': ac_name_list}

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
    
    context_dict = {'aakashcentres': ac_city_list}

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
    
    context_dict = {'aakashcentres': ac_state_list}

    return render_to_response('ac/ac_list.html',
                              context_dict, context)


def suggest_project_name(request):
    """Suggest project name on '/ac/projects/' | project_list.html page.
    
    Arguments:
    - `request`:

    """
    context = RequestContext(request)
    
    if request.method == 'GET':
        starts_with = request.GET['suggest_project_name']
        print "GET: suggestion"
        print starts_with
    else:
        print "POST: suggestion"
        starts_with = request.POST['suggest_project_name']

    project_list = get_project_list(10, starts_with)
    
    context_dict = {'projects': project_list}
    return render_to_response('ac/project_list.html',
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
        
    aakashcentre = AakashCentre.objects.get(pk=id)
    # print id
    # print aakashcentre.ac_id
    coordinator_name = aakashcentre.coordinator
    # print coordinator_name.id
    # print coordinator_name.user_id
    coordinator = Coordinator.objects.filter(id=coordinator_name.id)
    coordinator_detail = User.objects.get(id=coordinator_name.user_id)
    # print coordinator_detail.first_name

    projects = Project.objects.filter(approve=True, ac=id).order_by('-download_count')
    
    context_dict = {'aakashcentre': aakashcentre,
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

    projects = Project.objects.filter(approve=True).order_by('-download_count')
    context_dict = {'projects': projects}
    return render_to_response('ac/projects.html', context_dict, context)

def iitb(request):
    """List all projects at iitb.
    IITB has RC_ID=1000."""
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
        
    try:
        iitb = AakashCentre.objects.get(ac_id=1000)
        coordinator = iitb.coordinator
        coordinator = Coordinator.objects.filter(id=coordinator.id)
        projects = Project.objects.filter(approve=True, ac=iitb.id).order_by('-download_count')
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

        
    print id
    try:
        project = Project.objects.get(pk=id)
        members = TeamMember.objects.filter(member_project=id)
        print members
        mentors = Mentor.objects.filter(mentor_project=id)
        print mentors
    except:
        project = None
        members = None
        mentors = None
    
    context_dict = {'project': project,
                    'members': members,
                    'mentors': mentors}
    return render_to_response('ac/project.html', context_dict, context)


@login_required    
def project_add(request):
    """Add new project.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)

    MemberFormset = formset_factory(MemberForm,
                                    can_delete=False,
                                    extra=1)

    if request.method == 'POST':
        print "We got a request to add new project"
        projectform = ProjectForm(request.POST, request.FILES)
        memberformset = MemberFormset(request.POST)
        mentorform = MentorForm(request.POST)

        if projectform.is_valid() and memberformset.is_valid() and mentorform.is_valid():
            print "Add project form is valid."
            projectform = projectform.save(commit=False)
            #memberformset = memberformset.save(commit=False)
            mentorform = mentorform.save(commit=False)
            projectform.ac = AakashCentre.objects.get(name=projectform.ac)
            print projectform.name
            projectform.save()

            #TODO: If TeamMember &/OR Mentor values are NULL, don't save it.
            for form in memberformset.forms:
                memberform = form.save(commit=False)
                memberform.member_project = projectform
                memberform.save()
            # memberformset.member_project = projectform
            # memberformset.save()
            mentorform.mentor_project = projectform
            mentorform.save()
            messages.success(request, "Project successfully submitted. Waiting for approval.")
            return HttpResponseRedirect('/ac/project/add/')
        else:
            print projectform.errors, memberformset.errors, mentorform.errors
    else:
        projectform = ProjectForm()
        memberformset = MemberFormset()
        mentorform = MentorForm()

    context_dict = {'projectform': projectform,
                    'memberformset': memberformset,
                    'mentorform': mentorform}
    return render_to_response('ac/project_add.html', context_dict, context)


@login_required
def register(request):
    """Registeration Form.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)
    
    if request.method == 'POST':
        print "We've a request to register"
        aakashcentreform = AakashCentreForm(data=request.POST)
        coordinatorform = CoordinatorForm(data=request.POST)
        userform = UserForm(data=request.POST)

        if aakashcentreform.is_valid() and coordinatorform.is_valid() and userform.is_valid():
            print "Forms are Valid"
            user = userform.save(commit=False)
            print user.username
            print user.first_name
            user.set_password(user.password)
            user.save()

            coordinator = coordinatorform.save(commit=False)
            print coordinator.contact
            if 'picture' in request.FILES:
                coordinator.picture = request.FILES['picture']
            coordinator.user = User.objects.get(username=user.username)
            coordinator.save()
            
            aakashcentre = aakashcentreform.save(commit=False)
            aakashcentre.coordinator = Coordinator.objects.get(user=coordinator.user)
            aakashcentre.save()
            print aakashcentre.ac_id
            messages.success(request, "Form successfully submitted.")
            return HttpResponseRedirect('/ac/register/')
        else:
            if aakashcentreform.errors or coordinatorform.errors or userform.errors:
                print aakashcentreform.errors, coordinatorform.errors, userform.errors
    else:
        aakashcentreform = AakashCentreForm()
        coordinatorform = CoordinatorForm()
        userform = UserForm()
        
    context_dict = {'aakashcentreform': aakashcentreform,
                    'coordinatorform': coordinatorform,
                    'userform': userform}
    return render_to_response('ac/register.html', context_dict, context)

    
def user_login(request):
    """Login form.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/user/profile/')
            else:
                # An inactive account was used - no logging in!
                messages.info(request, "Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            messages.error(request, "Bad login.")
            return render_to_response('ac/login.html', context)
    else:
        return render_to_response('ac/login.html', context)


@login_required
def user_logout(request):
    """Logout user.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/')    
    

@login_required
def user_profile(request):
    """User profile."""
    context = RequestContext(request)
    return render_to_response('profile.html', context)
    
    
