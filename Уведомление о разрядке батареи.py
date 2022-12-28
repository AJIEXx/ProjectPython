# Библиотека psutil является мощным инструментом для аналитики всех запущенных процессов и мониторинга системы в целом. Как идея — сделать приложение для удаленного мониторинга нод и ежедневной отсылкой информации вам в телеграмм
#
# Пример с анализом уровня заряд батареи ноутбука, потребуется установить psutil

# pip install psutil
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 30 and plugged!=True:

    # pip install py-notifier
    # pip install win10toast
    from pynotifier import Notification

    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remain!!",
        duration=5,  # Duration in seconds

    ).send()