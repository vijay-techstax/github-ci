import os
from dotenv import load_dotenv

load_dotenv()

MODE = os.environ["MODE"]

if MODE == "DEVELOPMENT":
    try:
        from environment.dev.settings_config import *
    except ImportError:
        print("settings_config.py file not found")

elif MODE == "STAGING":
    try:
        from environment.staging.settings_config import *
    except ImportError:
        print("settings_config.py file not found")

elif MODE == "PRODUCTION":
    try:
        from environment.production.settings_config import *
    except ImportError:
        print("settings_config.py file not found")

else:
    print("Invalid MODE")
