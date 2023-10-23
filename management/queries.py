from management.models import *


def company_query():
    return Company.objects.all()
