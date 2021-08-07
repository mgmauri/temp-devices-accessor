from dependency_injector import containers, providers
from src.core.settings import settings


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration()
    silicon_thermals_config = providers.Configuration()
    gpio_config = providers.Configuration()


Configs.config.from_yaml(settings.EVKSCONFIGFILE)

Configs.silicon_thermals_config.from_dict({
        evk_name: data["com_number"]
        for evk_name, data in Configs.config().items()
    })
Configs.gpio_config.from_dict({
        evk_name: data["pin_number"]
        for evk_name, data in Configs.config().items()
    })
