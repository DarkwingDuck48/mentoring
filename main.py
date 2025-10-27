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


class ChildExample(Example):
    def __private_method(self):
        return 'child private method'


# Демонстрация name mangling
obj = Example()

print(obj.public)  # ✅ "public"
print(obj.public_method())  # ✅ public_method"


print(obj._protected)  # ✅ "prot" (но не рекомендуется)
print(obj._protected_method())  # ✅ "protected method" (но не рекомендуется)

# print(obj.__private)  # ❌ AttributeError
# print(obj.__private_method())  # ❌ AttributeError

# А вот так можно (но не нужно!)
print(obj._Example__private)  # ✅ "priv"
print(obj._Example__private_method())  # ✅ "private method"


print(' ===== CHILD ==== ')

child_obj = ChildExample()

print(child_obj.public)  # ✅ "public"
print(child_obj.public_method())  # ✅ public_method"


print(child_obj._protected)  # ✅ "prot" (но не рекомендуется)
print(child_obj._protected_method())  # ✅ "protected method" (но не рекомендуется)

# print(child_obj.__private)  # ❌ AttributeError
# print(child_obj.__private_method())  # ❌ AttributeError

# А вот так можно (но не нужно!)
# print(child_obj._ChildExample__private)  # ✅ "priv"
# print(child_obj._ChildExample__private_method())  # ✅ "private method"

# print(child_obj._Example__private)  # ✅ "priv"
# print(child_obj._Example__private_method())  # ✅ "private method"
