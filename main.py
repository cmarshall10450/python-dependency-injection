from services import Services, Configs
import json

def main():
  Services.config_loader().load_config("test.yaml")
  s3 = Services.s3()

  result = Services.pokemon().get_pokemon("ditto")
  s3.copy_from_bytes("test.json", json.dumps(result, indent=2))

main()