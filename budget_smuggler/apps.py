"""App loading functionality for budget_smuggler"""
from django.apps.config import AppConfig


class BudgetSmugglerAppConfig(AppConfig):
    """Application configuration for the main application"""
    name = 'budget_smuggler'
    verbose_name = 'Budget Smuggler'
