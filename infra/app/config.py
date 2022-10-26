import os
import json
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


class Config:
    __file = 'appsettings.json'
    __json = None

    @staticmethod
    def init():
        LOGGER.info('Configuring app settings')
        with open(Config.__file) as json_config_file:
            Config.__json = json.load(json_config_file)

    @staticmethod
    def is_dr() -> bool:
        dr = Config.__json['isDr'].lower()
        if dr == 'true':
            return True
        elif dr == 'false':
            return False
        else:
            raise Exception('isDr is not specified Correctly')

    @staticmethod
    def env() -> str:
        return Config.__json['env']

    @staticmethod
    def region() -> str:
        return Config.__json['region']

    @staticmethod
    def dr_region() -> str:
        return Config.__json['drRegion']

    @staticmethod
    def account() -> str:
        return Config.__json['account']

    @staticmethod
    def isMTLS() -> str:
        return Config.__json['MTLS']

    @staticmethod
    def shortName() -> str:
        return Config.__json['stackIdentifier']
