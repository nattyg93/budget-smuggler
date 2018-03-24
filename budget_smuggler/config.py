from dj_core_drf.config import Config as BaseConfig


class Config(BaseConfig):
    defaults = BaseConfig.defaults.copy()
    defaults.update([
        ('REST_FRAMEWORK__DEFAULT_RENDERER_CLASSES', (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.AdminRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        )),
    ])
