# Get list of rc_id, rc_name, city etc. for search.
from ac.models import AakashCenter, Project


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


def get_project_list(max_results=0, starts_with=''):
    if starts_with:
        lst = Project.objects.filter(name__contains=starts_with)
    else:
        lst = Project.objects.all()
    return lst
