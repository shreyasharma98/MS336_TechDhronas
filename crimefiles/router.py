class ModelDatabaseRouter(object):
    """Allows each model to set its own destiny"""

    def db_for_read(self, model, **hints):
        # Specify target database with field in_db in model's Meta class
        if model._meta.app_label == 'crimefiles':
            return 'crimefilesdata'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'crimefiles':
            return 'crimefilesdata'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        if obj1._meta.app_label == 'crimefiles' and obj2._meta.app_label == 'crimefiles':
            return True
        # Allow if neither is chinook app
        elif 'crimefiles' not in [obj1._meta.app_label, obj2._meta.app_label]:
                return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the Example app's models get created on the right database."""
        if app_label == 'crimefiles':
            # The Example app should be migrated only on the example_db database.
            return db == 'crimefilesdata'
        elif db == 'crimefilesdata':
            # Ensure that all other apps don't get migrated on the example_db database.
            return False

        # No opinion for all other scenarios
        return None

    # def allow_syncdb(self, db, model):
    #     if db == 'crimefilesdata' or model._meta.app_label == "crimefiles":
    #         return False # we're not using syncdb on our legacy database
    #     else: # but all other models/databases are fine
    #         return True
