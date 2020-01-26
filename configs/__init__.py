from dependency_injector import providers, containers

class Configs(containers.DeclarativeContainer):
    http = providers.Configuration('http')
    pokemon = providers.Configuration('pokemon')
    s3 = providers.Configuration('s3')
    sft = providers.Configuration('sftp')
