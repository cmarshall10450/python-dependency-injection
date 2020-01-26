class PokemonService:
  def __init__(self, config, http_service=None):
    self._config = config
    self.http = http_service

  def get_pokemon(self, pokemon):
    return self.http.get(f"{self._config['base_url']}/{pokemon}")