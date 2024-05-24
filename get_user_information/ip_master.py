import requests


class UserInfoChecker:
    """
    A class for get all info of user
    """
    def __init__(self):
        self.api_url: str = 'https://ipinfo.io/json'
        self.data: dict = self.__init()

    def __init(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data: dict = response.json()
            del data['readme']
        else:
            data: dict = {
                'ip': '',
                'hostname': '',
                'city': '',
                'region': '',
                'country': '',
                'loc': '',
                'org': '',
                'postal': '',
                'timezone': ''
            }
        return data

    def get_ip_address(self):
        """
        A func for get IP address of user
        :return: IP address
        """
        return self.data['ip']

    def get_hostname(self):
        """
        A func for get hostname of user
        :return: hostname
        """
        return self.data['hostname']

    def get_city(self):
        """
        A func for get city of user
        :return: city
        """
        return self.data['city']

    def get_region(self):
        """
        A func for get region of user
        :return: region
        """
        return self.data['region']

    def get_country(self):
        """
        A func for get country of user
        :return: country
        """
        return self.data['country']

    def get_loc(self):
        """
        A func for het location of user
        :return: location
        """
        return self.data['loc']

    def get_org(self):
        """
        A func for get organisation of user
        :return: organisation
        """
        return self.data['org']

    def get_postal(self):
        """
        A func for get postal of user
        :return: postal
        """
        return self.data['postal']

    def get_timezone(self):
        """
        A func for get timezone of user
        :return: timezone
        """
        return self.data['timezone']

    def all_user_info(self):
        """
        A func for get all info of user
        :return: IP address, hostname, city, region, country, location, organisation, postal, timezone
        """
        return self.data