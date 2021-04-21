import os


class ReadEnvironment:
    @staticmethod
    def get_concert_user_name():
        return os.environ['C_User']

    @staticmethod
    def get_concert_password():
        return os.environ['password']

