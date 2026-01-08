import sys
import os
import shutil

# 1. PROGRAMMATICALLY DISABLE PYCACHE
# This ensures no bytecode is generated unless you are in 'production'
if os.environ.get('FLASK_ENV') != 'production':
    sys.dont_write_bytecode = True

from app import create_app
from app.config import DevelopmentConfig

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    app.run(debug=True)

