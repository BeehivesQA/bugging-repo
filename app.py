import sys
config = {"port": 8080}
print("starting server on port", config["port"])
print("database url:", config.get("database_url"))
sys.exit(0)
