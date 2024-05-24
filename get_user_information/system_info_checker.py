import os


class SystemInfoChecker:
    @classmethod
    def get_username(cls):
        return os.getlogin()
