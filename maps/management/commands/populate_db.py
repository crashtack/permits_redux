# http://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
from django.core.management.base import BaseCommand
from django.db import IntegrityError
import json
from maps.models import Permit, PermitOwner
from permits_redux.settings import BASE_DIR, GEOIP_PATH
from django.contrib.auth.models import User
# from math import floor
# import sys
import os
# sys.path.append(os.path.join(os.environ.get('PWD', ''), 'permit_user'))
# from permit_user.models import PermitUser


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _save_permit_to_database(self):
        """Add a permit to the database"""

        #file_path = 'media/contruction.json'
        file_path = os.path.join(GEOIP_PATH, 'contruction.json')
        # permit_user = PermitOwner.objects.filter(user=1).first()
        owner = User.objects.all().first()
        with open(file_path, 'r') as f:
            data = json.load(f)

        count = 0
        for perm in data:
            if perm.get('final_date') is None and perm.get('latitude') and perm.get('longitude'):

                if perm.get('description'):
                    if len(perm.get('description')) >= 255:
                        perm['description'] = perm.get('description')[0:255]

                permit = Permit(
                    # permit_user=permit_user,
                    owner=owner,
                    permit_number=perm['application_permit_number'],
                    latitude=perm['latitude'],
                    longitude=perm['longitude'],
                    master_use_permit=perm.get('master_use_permit'),
                    action_type=perm.get('action_type'),
                    address=perm.get('address'),
                    applicant_name=perm.get('applicant_name'),
                    application_date=perm.get('application_date'),
                    issue_date=perm.get('issue_date'),
                    final_date=perm.get('final_date'),
                    experation_date=perm.get('experation_date'),
                    category=perm.get('category'),
                    description=perm.get('description'),
                    url=perm.get('permit_and_complaint_status_url'),
                    permit_type=perm.get('permit_type'),
                    status=perm.get('status'),
                    value=float(perm.get('value')),
                    work_type=perm.get('work_type'),
                    contractor=perm.get('contractor'),
                )
                try:
                    print("Count: {} Adding permit to DB: {}".format(count, perm.get('application_permit_number')))
                    permit.save()
                    # print()
                except IntegrityError:
                    print("Count: {} Premit {} is already in the database".format(count, perm.get('application_permit_number')))
                    pass

                count += 1

            # uncomment to only add x number of permit
            # x = 100
            # if count >= x:
            #     return

        print('count: {}'.format(count))

    def _list_permits():
        pass

    # def _list_permit_user(self):
    #     pu = PermitUser.objects.filter(user=1).first()
    #     print("Permit User: {}".format(pu.user.username))

    def _hello(self):
        """ Say Hello """
        print('hello\n')
        print(BASE_DIR)
        print(GEOIP_PATH)

    def handle(self, *args, **options):
        self._hello()
        # self._list_permit_user()
        self._save_permit_to_database()
