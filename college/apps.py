from django.apps import AppConfig


class CollegeConfig(AppConfig):
    name = 'college'
    def ready(self): # jab project run hoga to ready method call hoga jo mysignal file ko import kardega hamare project me
        import college.mysignal
