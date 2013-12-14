import os
import sys
import store
import coordinators_list
import ac_list


def populate_users():

    # Admin
    os.system("python manage.py syncdb --noinput")
    os.system("python manage.py createsuperuser --username=admin --email=admin@example.com")
    """
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
    """
def populate_ac():

    for ac in ac_list.acs:
        print "Adding AC: %s has coordinator: %s" % (ac['NAME'], ac['COORDINATOR'])
        add_ac(
            ac_id=ac['RC_ID'],
            name=ac['NAME'],
            coordinator=User.objects.get(username=ac['COORDINATOR']),
            city=ac['CITY'],
            state=ac['STATE'],
            status=True)


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

def add_ac(ac_id, name, city, state, coordinator, status):
    ac = AakashCentre(ac_id=ac_id, name=name, city=city,
                      state=state, coordinator=coordinator,
                      status=status)
    ac.save()

def add_faq(question, answer):
    faq = Faq(question=question, answer=answer)
    faq.save()
    
# start execution here!
if __name__ == '__main__':
    print "Starting Aakashlabs population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aakashlabs.settings')
    from ac.models import AakashCentre, Coordinator
    from ac.models import Faq
    from django.contrib.auth.models import User

    if os.path.exists('ac.db'):
        os.system("rm ac.db")

    populate_users()
    # populate_ac()
    populate_faq()
