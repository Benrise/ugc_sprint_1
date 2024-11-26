#!/bin/bash

alembic upgrade head

python create_roles.py

python create_superuser.py "$AUTH_SUPERUSER_USERNAME" "$AUTH_SUPERUSER_PASSWORD"

python main.py