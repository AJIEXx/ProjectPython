# Если перейти на google.com является для тебя тяжелой задачей, тебя могут спасти эти 3 строчки кода.
#
# Чтобы всё работало как швейцарские часы --> pip install google

from googlesearch import search
query = "best hentai videos with Asynco and Max Wayld"

for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)