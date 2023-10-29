class Government:
    __instance = None

    def __init__(self):
        if Government.__instance is None:
            Government.__instance = self

        else:
            raise Exception("You cannot create another government")

    @staticmethod
    def get_instance():
        if not Government.__instance:
            Government()
        return Government.__instance


govt = Government()
print(govt)

second_govt = Government.get_instance()
print(second_govt)

third_govt = Government.get_instance()
print(third_govt)

new_govt = Government()
print(new_govt)
