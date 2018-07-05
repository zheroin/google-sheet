import os

import pygsheets
from pygsheets.client import Client

from googleapiclient.http import HttpError


class TestAuthorization(object):

    def setup_class(self):
        self.base_path = os.path.join(os.path.dirname(__file__), 'auth_test_data')

    def test_service_account_authorization(self):
        c = pygsheets.authorize(service_account_file=self.base_path + '/pygsheettest_service_account.json')
        assert isinstance(c, Client)

        self.sheet = c.create('test_sheet')
        self.sheet.share('pygsheettest@gmail.com')
        self.sheet.delete()

    def test_user_credentials_loading(self):
        c = pygsheets.authorize(client_secret=self.base_path + '/client_secret.json',
                                credentials_directory=self.base_path)
        assert isinstance(c, Client)

        self.sheet = c.create('test_sheet')
        self.sheet.share('pygsheettest@gmail.com')
        self.sheet.delete()

    def teardown_class(self):
        c = pygsheets.authorize(service_account_file=self.base_path + '/pygsheettest_service_account.json')
        sheets = c.open_all()
        for sheet in sheets:
            sheet.delete()

        c = pygsheets.authorize(client_secret=self.base_path + '/client_secret.json',
                                credentials_directory=self.base_path)
        sheets = c.open_all()
        for sheet in sheets:
            try:
                sheet.delete()
            except HttpError as err:
                # do not delete files which the test suite has no permission for.
                if err.resp['status'] == '403':
                    pass
                else:
                    raise