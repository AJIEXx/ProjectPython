# Классический пример генерации простых паролей заданной длины. Будет полезен для написания авторегеров почт или аккаунтов в тот же Sandbox.
#
# Дополнительных библиотек не нужно, пароль генерируется из чисел, символов и букв

import random
import string
total = string.ascii_letters + string.digits + string.punctuation
length = 16
password = "".join(random.sample(total, length))
print(password)