from dapr.clients import DaprClient

# Learn more: https://docs.dapr.io/getting-started/quickstarts/configuration-quickstart/
DAPR_SECRET_STORE = "local_secret_store"
CONFIG_NAME = "DB_NAME"

with DaprClient() as client:
    config = client.get_configuration(store_name=DAPR_SECRET_STORE, keys=[CONFIG_NAME], config_metadata={})
    print(f"Configuration for {CONFIG_NAME} : {config.items[CONFIG_NAME]}", flush=True)
