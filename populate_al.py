import os
import sys
import store
import coordinators_list
import ac_list
import project_list

def populate_users():
    """Populate Coordinators."""
    # Admin
    os.system("python manage.py syncdb --noinput")
    # os.system("python manage.py schemamigration ac --initial")
    # os.system("python manage.py migrate ac")    
    os.system("python manage.py createsuperuser --username=admin --email=admin@example.com")

    for u in coordinators_list.users:
        # Normal users
        print "Adding user: %s" % u['USERNAME']
        u['USERNAME'] = add_user(u['USERNAME'],
                                 u['FIRSTNAME'],
                                 u['LASTNAME'],
                                 u['EMAIL'],
                                 u['PASSWORD'],)
        
        add_coordinator(user=u['USERNAME'],
                        contact=u['CONTACT'],
                        picture=u['PHOTO'])

    user_list = User.objects.all()
    if user_list:
        print "Following user(s) created successfully."
        for i in user_list:
            print i.username


def populate_ac():
    """Populate Aakash Centres."""
    for ac in ac_list.acs:
        print "Adding AC: %s has coordinator: %s" % (ac['NAME'], ac['COORDINATOR'])
        usr_instance = User.objects.get(username=ac['COORDINATOR'])
        coordinator_instance = Coordinator.objects.get(user=usr_instance)
        add_ac(
            ac_id=ac['RC_ID'],
            name=ac['NAME'],
            coordinator=coordinator_instance,
            city=ac['CITY'],
            state=ac['STATE'],
            active=True)


def populate_project():
    """Populate projects."""

    print "Populating projects.."
    for project in project_list.projects:
        if project['AC_ID'] == "0":
            print "Project: %s doest not have a valid AC_ID." % project['NAME']
        else:
            print "RC_ID: %s" % project['AC_ID']
            print "Project name: %s" % project['NAME'][:1].upper() + project['NAME'][1:].lower()
        
            inst_name = AakashCentre.objects.get(ac_id=project['AC_ID'])
            member = TeamMember(name=project['MEMBER'], email=project['MEMBER_EMAIL'])
            member.save()

            demo = Project(
                name=project['NAME'][:1].upper() + project['NAME'][1:].lower(),
                ac=inst_name,
                summary=project['DESCRIPTION'],
                src_url=project['SRC_CODE'],
                doc_url="",
                approve=True)

            demo.save()
            demo.member.add(member)
        
    """"
    # working
    inst_name = AakashCentre.objects.get(ac_id=1002)

    sachin = TeamMember(name="sachin", email="isachin@github.com")
    sachin.save()

    ac = AakashCentre.objects.get(ac_id=1001)
    demo = Project(name="demo", ac=inst_name, summary="demo desc.",
                   src_url="http://google.com", doc_url="http://google.com")
    demo.save()
    demo.member.add(sachin)
    """


def populate_faq():
    """Populate FAQs.
    """
    q1 = add_faq(
        
        question="I have forgotten the pattern set by me, how can I login to Aakash tablet?",
        
        answer="""
1. Foremost make sure that you USB debugging is enabled.
2. Connect your tablet to the computer.

        For Window User.
3. Go to the Start option. Open command prompt. Type cmd and press enter.
4. A window will pop up with a C: prompt.
        Ex :-   C:\Users\user>
5. Type the following commands
        C:\Users\user>adb shell
        sh-3.2# rm/data/system/gesture.key
        rm/data/system/gesture.key
        sh-3.2#

        Once this is done, one has to restart/reboot their tablet. Now
        the tablet is ready to use.
        
        For Ubuntu User.
        
6. Go to the terminal.
7. Then go to the folder where adb is installed.
8. Repeat the commands from step number 5.

        In addition to the above steps, a link has been provided for
your reference(http://www.youtube.com/watch?v=QYdkgO1KHmk)"""
    )

def add_user(username, first_name, last_name, email, password):
    u = User.objects.create_user(username=username, first_name=first_name,
                                 last_name=last_name,
                                 email=email, password=password)
    return u


def add_coordinator(user, contact, picture):
    up = Coordinator(user=user, contact=contact, picture=picture)
    up.save()

def add_ac(ac_id, name, city, state, coordinator, active):
    ac = AakashCentre(ac_id=ac_id, name=name, city=city,
                      state=state, coordinator=coordinator,
                      active=active)
    ac.save()


def add_faq(question, answer):
    faq = Faq(question=question, answer=answer)
    faq.save()


def add_project(name, ac, summary, team_member, src_url, doc_url=None,
                approve=False):
    project = Project(name=name, ac=ac, summary=summary,
                      src_url=src_url, doc_url=doc_url, approve=approve)
    project.save()
    project.member.add(team_member)


def add_member(name, email):
    member = TeamMember(name=name, email=email)
    member.save()

    
# start execution here!
if __name__ == '__main__':
    print "Starting Aakashlabs population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aakashlabs.settings')
    from ac.models import AakashCentre, Coordinator
    from ac.models import Faq
    from ac.models import Mentor, TeamMember, Project
    from django.contrib.auth.models import User

    if os.path.exists('ac.db'):
        os.system("rm ac.db")

    populate_users()
    populate_ac()
    populate_faq()
    populate_project()
