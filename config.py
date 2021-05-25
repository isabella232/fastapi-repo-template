import os


class Settings:
    debug = bool(os.environ.get('Debug', False))
    autoreload = True
    root_path = ''
    service_host = 'localhost'
    service_port: int = 13050
    log_level = 'DEBUG'
    logs_file: str = 'configs_service_default.log'


settings = Settings()
