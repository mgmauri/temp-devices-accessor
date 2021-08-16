from dependency_injector import containers, providers
from src.core.settings import settings


class DriversConfig(containers.DeclarativeContainer):
    config = providers.Configuration()
    silicon_thermals_config = providers.Configuration()
    gpio_config = providers.Configuration()


DriversConfig.config.from_yaml(settings.DRIVERSCONFIGFILE)
DriversConfig.silicon_thermals_config.from_dict({
        evk_name: data["port"]
        for evk_name, data in DriversConfig.config().items()
    })
DriversConfig.gpio_config.from_dict({
        evk_name: data["pin_number"]
        for evk_name, data in DriversConfig.config().items()
    })


class OperationConfig(containers.DeclarativeContainer):
    config = providers.Configuration()


OperationConfig.config.from_yaml(settings.OPERATIONCONFIGFILE)
