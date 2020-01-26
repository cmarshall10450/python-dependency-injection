from dependency_injector import providers, containers
from .http import HttpService
from .pokemon import PokemonService
from .config_loader import ConfigLoaderService
from .s3 import S3Service
from configs import Configs
    
class Services(containers.DeclarativeContainer):
    config_loader = providers.Singleton(ConfigLoaderService)
    http = providers.Singleton(HttpService, Configs.http)
    pokemon = providers.Singleton(PokemonService, Configs.pokemon, http_service=http)
    s3 = providers.Singleton(S3Service, Configs.s3)
