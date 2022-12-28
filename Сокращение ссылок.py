# Чтобы не использовать сторонние сервисы по типу bit.ly, ты всегда можешь сделать собственную "сокращалку" в пару строчек.
#
# Надо будет установить pyshorteners --> (тык)

import pyshorteners

s=pyshorteners.Shortener()
url = "type your hentai videos here"

print(s.tinyurl.short(url))