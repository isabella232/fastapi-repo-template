import os
from cc_tools.settings.base import BaseSettings
from cc_tools.settings.redis import RedisSettings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Settings(RedisSettings, BaseSettings):
    class Config:
        env_file = os.path.join(BASE_DIR, '.env')

    debug = bool(os.environ.get('Debug', False))
    base_dir: str = BASE_DIR
    autoreload = True
    root_path = ''
    service_host = 'localhost'
    service_port: int = 13050
    log_level = 'DEBUG'
    logs_file: str = 'configs_service_default.log'
    database_url: str


settings = Settings()
