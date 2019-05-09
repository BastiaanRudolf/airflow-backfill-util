# -*- coding: utf-8 -*-

# Inbuilt Imports
from flask import Blueprint
from airflow.plugins_manager import AirflowPlugin

# Backfill Plugin Imports
from backfill.main import Backfill

# Init the plugin in Webserver's "Admin" Menu with Menu Item as "Backfill"
backfill_admin_view = Backfill(category="Admin", name="Backfill")

# Creating a flask blueprint to integrate the templates folder
backfill_blueprint = Blueprint(
    "backfill_blueprint", __name__,
    template_folder='templates')

# Defining the plugin class
class AirflowBackfillPlugin(AirflowPlugin):
    name = "backfill_plugin"
    admin_views = [backfill_admin_view]
    flask_blueprints = [backfill_blueprint]