class Example:
    def __init__(self):
        self.public = 'public'  # public
        self._protected = 'prot'  # protected
        self.__private = 'priv'  # private

    def public_method(self):
        return 'public method'

    def _protected_method(self):
        return 'protected method'

    def __private_method(self):
        return 'private method'


# Демонстрация name mangling
obj = Example()

print(obj.public)  # ✅ "public"
print(obj._protected)  # ✅ "prot" (но не рекомендуется)

# print(obj.__private)        # ❌ AttributeError
# print(obj.__private_method) # ❌ AttributeError

# А вот так можно (но не нужно!)
print(obj._Example__private)  # ✅ "priv"
print(obj._Example__private_method())  # ✅ "private method"
