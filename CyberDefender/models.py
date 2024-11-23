from django.db import models
from django.utils import timezone


class UserVisit(models.Model):
    ip_address = models.CharField(max_length=100, db_column='ip_address')
    country = models.CharField(max_length=100, db_column='country')
    city = models.CharField(max_length=100, db_column='city')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, db_column='latitude')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, db_column='longitude')
    postal_code = models.CharField(max_length=20, db_column='postal_code')
    network = models.CharField(max_length=100, db_column='network')
    browser = models.CharField(max_length=100, db_column='browser')
    browser_version_string = models.CharField(max_length=100, db_column='browser_version')
    device = models.CharField(max_length=100, db_column='device')
    user_agent = models.TextField(max_length=256, db_column='user_agent')
    cookies = models.TextField(max_length=256, db_column='cookies')
    timestamp = models.DateTimeField(default=timezone.now, db_column='timestamp')

    class Meta:
        db_table = 'cyberdefender_uservisit'

    def __str__(self):
        return f"Visit from {self.ip_address} at {self.timestamp}"


'''
class UserVisit(models.Model):
    ip_address = models.CharField(max_length=100, verbose_name="ip_address")
    country = models.CharField(max_length=100, verbose_name="country")
    city = models.CharField(max_length=100, verbose_name="City")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="longitude")
    postal_code = models.CharField(max_length=20, verbose_name="postal_code")
    network = models.CharField(max_length=100, verbose_name="network")
    browser = models.CharField(max_length=100, verbose_name="browser")
    browser_version_string = models.CharField(max_length=100, verbose_name="browser_version")
    device = models.CharField(max_length=100, verbose_name="device")
    user_agent = models.TextField(max_length=256, verbose_name="user_agent")
    cookies = models.TextField(max_length=256, verbose_name="cookies")
    timestamp = models.DateTimeField(default=timezone.now, verbose_name="timestamp")

    class Meta:
        db_table = 'cyberdefender_uservisit'

    def __str__(self):
        return f"Visit from {self.ip_address} at {self.timestamp}"


class UserVisit(models.Model):
    ip_address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    postal_code = models.CharField(max_length=20)
    network = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    browser_version_string = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    user_agent = models.TextField(max_length=256)
    cookies = models.TextField(max_length=256)
    timestamp = models.DateTimeField(default=timezone.now)  # Додано поле дати та часу заходу на веб-сайт

    def __str__(self):
        return f"Visit from {self.ip_address} at {self.timestamp}"
'''


def save_user_visit(user_ip, country, city, latitude, longitude, postal_code, network, browser, browser_version_string, device, user_agent, cookies):
    # Створення нового об'єкта UserVisit з переданими даними та поточним часом
    user_visit = UserVisit.objects.create(
        ip_address=user_ip,
        country=country,
        city=city,
        latitude=latitude,
        longitude=longitude,
        postal_code=postal_code,
        network=network,
        browser=browser,
        browser_version_string=browser_version_string,
        device=device,
        user_agent=user_agent,
        cookies=cookies,
        timestamp=timezone.now()  # Встановлення поточної дати та часу
    )
    # Збереження об'єкта в базі даних
    user_visit.save()