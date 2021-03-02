#!/bin/sh

cp .env.example .env
cp environment/dev/settings_config.example environment/dev/settings_config.py
cp environment/staging/settings_config.example environment/staging/settings_config.py
cp environment/prod/settings_config.example environment/prod/settings_config.py
