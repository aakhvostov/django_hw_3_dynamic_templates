from datetime import datetime, timedelta
from time import time
from django import template


register = template.Library()


@register.filter
def format_date(value):
    dt = int(str(value)[:-2])
    now = int(time())
    duration = timedelta(seconds=(now - dt))
    if duration.seconds / 60 < 10:
        value = "только что"
    elif duration.seconds / 3600 < 24:
        value = f"{round(duration.seconds / 3600)} часов назад"
    else:
        value = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d')
    return value


@register.filter
def score_show(value):
    if int(value) < -5:
        value = "всe плохо"
    elif -5 <= int(value) < 5:
        value = "нейтрально"
    else:
        value = "хорошо"
    return value


@register.filter
def format_num_comments(value):
    if int(value) == 0:
        value = 'Оставьте комментарий'
    elif int(value) > 50:
        value = '50+'
    return value
