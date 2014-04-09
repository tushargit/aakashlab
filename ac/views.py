from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.core.mail import send_mail

# Models
from ac.models import AakashCentre, Coordinator
from ac.models import Project, Mentor, TeamMember
from ac.models import Faq, Pub

# Forms
from ac.forms import ContactForm, AakashCentreForm
from ac.forms import CoordinatorForm, UserForm
from ac.forms import ProjectForm, Agreement
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

def introduction(request):
    """Introduction page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('home/introduction.html', context)

def proposal(request):
    """Proposal page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('home/proposal.html', context)

def history(request):
    """History page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('home/history.html', context)

def configuration(request):
    """Configuration page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('home/configuration.html', context)

def distribution(request):
    """Tablet Distribution and Testing page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('home/distribution.html', context)

def training(request):
    """Training and Contest page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('home/training.html', context)

def sidebar_projects(request):
    """RnD page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('home/sidebar_projects.html', context)


def research(request):
    """RnD page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('home/research.html', context)

def future(request):
    """Future of Aakash page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('home/future.html', context)

def privacy(request):
    """Privacy of Aakash labs.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)    
    return render_to_response('privacy.html', context)

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
            email_subject = "[Contact Us] aakashlabs.org"
            email_message = "Sender Name: " + contactform.name + "\n\n" + contactform.message
            send_mail(email_subject, email_message,
                      contactform.email,
                      [
                          'iclcoolster@gmail.com',
                          'Aakashprojects.iitb@gmail.com',
                      ],
                      fail_silently=False)
            messages.success(request, "Thank you for your reply. We\
            will get back to you soon.")
        else:
            print contactform.errors
            messages.error(request, "One or more fields are required or not valid.")
    else:
        contactform = ContactForm()

    context_dict = {'contactform': contactform}
    return render_to_response('contact.html', context_dict, context)


def gnu(request):
    """
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)
    return render_to_response('gnu.html', context)


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

def activities(request):
    """links of all the activites by IITB related to Aakash.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)    
    return render_to_response('activities.html', context)

def tutorials(request):
    """Tutorial page
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)    
    return render_to_response('tutorials.html', context)

def news(request):
    """news page.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)    
    return render_to_response('news.html', context)

def sitemap(request):
    """sitemap page.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)    
    return render_to_response('sitemap.html', context)

def others(request):
    """links of all the activites by others related to Aakash.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)    
    return render_to_response('other_activities.html', context)


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
    print request.user
    
    try:
        coordinator = Coordinator.objects.get(user=request.user)
        ac = AakashCentre.objects.get(coordinator=coordinator)
        print ac, ac.ac_id
    except:
        ac = None

    # I'm not sure about 'extra' argument if it is needed.
    MemberFormset = formset_factory(MemberForm,
                                    can_delete=False,
                                    extra=1)

    MentorFormset = formset_factory(MentorForm,
                                    can_delete=False,
                                    extra=1)

    if request.method == 'POST':
        print "We got a request to add new project."
        projectform = ProjectForm(request.POST, request.FILES)
        memberformset = MemberFormset(request.POST, prefix="member")
        mentorformset = MentorFormset(request.POST, prefix="mentor")
        agreement = Agreement(request.POST)

        if projectform.is_valid() and memberformset.is_valid() and mentorformset.is_valid() and agreement.is_valid():
            print "Add-New-Project form: is valid."
            projectform = projectform.save(commit=False)
            projectform.ac = AakashCentre.objects.get(pk=projectform.ac_id)
            print projectform.name
            projectform.save()

            # FIXME: If TeamMember &/OR Mentor values are NULL, don't
            # save it.  I'm not sure about 'empty_permitted'
            # attribute. Till then let 'has_changed' do the work.
            for form in memberformset.forms:
                if form.has_changed(): # Don't store empty values
                    memberform = form.save(commit=False)
                    memberform.member_project = projectform
                    memberform.save()
	    
            for form in mentorformset.forms:
                if form.has_changed(): # Don't store empty values
                    mentorform = form.save(commit=False)
                    mentorform.mentor_project = projectform
                    mentorform.save()

            email_subject="New Project has been added."
            email_message="""
New Project has been added.

Details:
Name: """ + projectform.name + """
AC_ID: """ + projectform.ac.ac_id + """
Aakash Centre: """ + projectform.ac.name + """

Waiting for your approval"""
            send_mail(email_subject, email_message,
                      'support@aakashlabs.org',
                      [
                          'iclcoolster@gmail.com',
                          'Aakashprojects.iitb@gmail.com',
                      ],
                      fail_silently=False)
            messages.success(request, "Project successfully submitted. Waiting for approval.")
            return HttpResponseRedirect('/ac/project/add/')
        else:
            print projectform.errors, memberformset.errors, mentorformset.errors
    else:
        projectform = ProjectForm()
        # Centre name will be selected by default for Coordinators.
        if ac:
            projectform.fields['ac'].queryset = AakashCentre.objects.filter(ac_id=ac.ac_id)
            
        agreement = Agreement()
        memberformset = MemberFormset(prefix="member")
        mentorformset = MentorFormset(prefix="mentor")

    context_dict = {'projectform': projectform,
                    'agreement': agreement,
                    'memberformset': memberformset,
                    'mentorformset': mentorformset}
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
            email_subject="New Aakash Center has been registered."
            email_message="""
New Aakash Center has been registered.

Details:
Name: """ + aakashcentre.name + """
City: """ + aakashcentre.city + """
State: """ + aakashcentre.state + """
Coordinator's Name: """ + coordinator.name.first_name + coordinator.name.last_name + """

Waiting for you approval"""
            send_mail(email_subject, email_message,
                      'support@aakashlabs.org',
                      [
                          'iclcoolster@gmail.com',
                          'Aakashprojects.iitb@gmail.com',
                      ],
                      fail_silently=False)
            messages.success(request, "Form successfully submitted. Waiting for\
            activation from admin.")
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
            messages.error(request, "Bad login!")
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


@login_required
def user_profile_edit(request):
    """Edit user's/Coordinators profile.

    Arguments:
    - `request`:
    """
    context = RequestContext(request)
    print request.user
    user = get_object_or_404(User, username=request.user)
    old_username = user.username
    print user.first_name
    print user.last_name

    coordinator = get_object_or_404(Coordinator, user=request.user)
    print coordinator.contact
    print coordinator.picture

    aakashcentre = get_object_or_404(AakashCentre, coordinator=coordinator)
    print aakashcentre.name

    if request.method == 'POST':
        print "We've a request to register"
        #aakashcentreform = AakashCentreForm(data=request.POST)
        coordinatorform = CoordinatorForm(data=request.POST, instance=coordinator)
        userform = UserForm(data=request.POST, instance=user)

        if coordinatorform.is_valid() and userform.is_valid():
            print "Forms are Valid"
            user = userform.save(commit=False)
            if old_username == user.username:
                print "Username unchanged"
            else:
                print "Username changed!. Deactivating old user."
                old_username = get_object_or_404(User, username=old_username)
                old_username.is_active = False
                old_username.save()
            # print user.username
            # print user.first_name
            # print user.last_name
            user.set_password(user.password)
            user.save()

            coordinator = coordinatorform.save(commit=False)
            # print coordinator.contact
            if 'picture' in request.FILES:
                coordinator.picture = request.FILES['picture']
            coordinator.user = User.objects.get(username=user.username)
            coordinator.save()

            # Save Aakash Centre details with the new Coordinator's profile.
            # aakashcentre = aakashcentreform.save(commit=False)
            aakashcentre.coordinator = Coordinator.objects.get(user=coordinator.user)
            aakashcentre.save()
            print aakashcentre.ac_id

            messages.success(request, "Profile updated successfully.")
            # return HttpResponseRedirect('/user/profile/')
        else:
            if coordinatorform.errors or userform.errors:
                print coordinatorform.errors, userform.errors
    else:
        # aakashcentreform = AakashCentreForm(instance=aakashcentre)
        coordinatorform = CoordinatorForm(instance=coordinator)
        userform = UserForm(instance=user)

    context_dict = {'coordinatorform': coordinatorform,
                    'userform': userform}
    return render_to_response('profile_edit.html', context_dict, context)
