import yaml
from configs import Configs

class ConfigLoaderService:
  def load_config(self, file_path):
    with open(file_path, "r") as f:
      config = yaml.safe_load(f)
    for connector_name, connector_config in config.items():
      getattr(Configs, connector_name).override(connector_config)
