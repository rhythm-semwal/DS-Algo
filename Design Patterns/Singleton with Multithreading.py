import threading


class Singleton:
    __singleton_lock = threading.Lock()
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            with Singleton.__singleton_lock:
                if not Singleton.__instance:
                    Singleton.__instance = self

        else:
            raise Exception("Cannot create new object")

    @staticmethod
    def get_instance():
        if not Singleton.__instance:
            Singleton()
        return Singleton.__instance


if __name__ == "__main__":
    class X(Singleton):
        pass


    class Y(Singleton):
        pass


    A1, A2 = X.get_instance(), X.get_instance()
    B1, B2 = Y.get_instance(), Y.get_instance()

    # assert A1 is not B1
    # assert A1 is A2
    # assert B1 is B2

    print('A1 : ', A1)
    print('A2 : ', A2)
    print('B1 : ', B1)
    print('B2 : ', B2)