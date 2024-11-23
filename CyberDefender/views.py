#from django.shortcuts import render
from user_agents import parse
import geoip2
import geoip2.database
import geoip2.errors
import ipaddress


#from django.http import HttpResponse
#from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import SignUpForm
from .models import save_user_visit
from . import plotly_app
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.forms import UserCreationForm

from django.conf import settings

# Отримуємо значення змінної NETWORK з налаштувань Django
network = settings.NETWORK


'''
GEOIP_PATH = '/home/student27/CyberDefender/GeoIP/GeoLite2-City.mmdb'

def home(request):
    #user_ip = request.META.get('REMOTE_ADDR', None)  # Отримання IP-адреси користувача
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR', None)

    # Отримати значення куки з ім'ям 'my_cookie'
    my_cookie_value = request.COOKIES.get('my_cookie', None)

    ua_string = request.META.get('HTTP_USER_AGENT', None)

    user_agent = parse(ua_string)

    # Accessing user agent's browser attributes
    #user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    #user_agent.browser.family  # returns 'Mobile Safari'
    #user_agent.browser.version  # returns (5, 1)
    #user_agent.browser.version_string   # returns '5.1'

    # Accessing user agent's operating system properties
    #user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
    #user_agent.os.family  # returns 'iOS'
    #user_agent.os.version  # returns (5, 1)
    #user_agent.os.version_string  # returns '5.1'
    #print("Браузер:", user_agent.browser.family)
    #print("Версія браузера:", user_agent.browser.version_string)
    #print("Операційна система:", user_agent.os.family)
    #print("Пристрій:", user_agent.device.family)

    #user_agent.is_mobile # returns True
    #user_agent.is_tablet # returns False
    #user_agent.is_touch_capable # returns False
    #user_agent.is_pc # returns False
    #user_agent.is_bot # returns False


    if user_ip:
        # URL веб-сервісу GeoIP
        #geoip_api_url = f'https://api.geoipify.com/v1/?ip={user_ip}&apiKey=YOUR_API_KEY'
        #geoip_api_url = f'http://ip-api.com/json/{user_ip}'
        #response = requests.get(f'http://ip-api.com/json/{ip_address}')

        # Ініціалізуємо об'єкт для використання бази даних GeoIP
        geoip_reader = geoip2.database.Reader(GEOIP_PATH)

        try:

           # Отримуємо інформацію про IP-адресу
            response = geoip_reader.city(user_ip)
            country = response.country.name
            city = response.city.name
            latitude = response.location.latitude
            longitude = response.location.longitude
            postal_code = response.postal.code
            network = response.traits.network
            browser = user_agent.browser.family
            browser_version_string = user_agent.browser.version_string
            device = user_agent.device.family


            # Передаємо інформацію в контекст шаблону
            context = {
                'user_ip': user_ip,
                'country': country,
                'city': city,
                'latitude': latitude,
                'longitude': longitude,
                'postal_code':postal_code,
                'network':network,
                'user_agent': ua_string,
                'my_cookie_value': my_cookie_value,
                'browser':browser,
                'browser_version_string':browser_version_string,
                'device':device,

            }

#response.country.iso_code
#response.subdivisions.most_specific.name
#response.subdivisions.most_specific.iso_code

#response.autonomous_system_number
#response.autonomous_system_organization

#https://github.com/maxmind/GeoIP2-python#city-database


        except geoip2.errors.AddressNotFoundError:
            # Обробляємо випадок, коли IP-адресу не вдалося знайти в базі даних GeoIP
            context = {
                'user_ip': user_ip,
                'country': None,
                'city': None,
                'latitude': None,
                'longitude': None,
                'postal_code':None,
                'network':None,
                'user_agent': ua_string,
                'my_cookie_value': my_cookie_value,
                'browser':browser,
                'browser_version_string':browser_version_string,
                'device':device,
            }

        return render(request, 'home.html', context)

    return render(request, 'home.html', context)  # Передача IP-адреси в шаблон

'''

# Create your views here.
#class HomePageView(TemplateView):

#    template_name = 'index.html'

#    def get(self, request, *args, **kwargs):
#        return render(request, self.template_name, context=None)



class HomePageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # Отримання IP-адреси користувача
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR', None)

        # Отримання значення куки з ім'ям 'my_cookie'
        my_cookie_value = request.COOKIES.get('my_cookie', None)


        # Перевірка, чи my_cookie_value є None, і якщо так, встановлення його на порожній рядок
        if my_cookie_value is None:
             my_cookie_value = ""

        # Отримання рядка user-agent та розбір його за допомогою бібліотеки user_agents
        ua_string = request.META.get('HTTP_USER_AGENT', None)
        user_agent = parse(ua_string)

        # Ініціалізуємо контекст для передачі в шаблон
        context = {}

        if user_ip:
            # Якщо є IP-адреса, виконуємо операції з GeoIP
            GEOIP_PATH = '/home/student27/CyberDefender/GeoIP/GeoLite2-City.mmdb'
            geoip_reader = geoip2.database.Reader(GEOIP_PATH)
            try:
                response = geoip_reader.city(user_ip)
                context.update({
                    'user_ip': user_ip,
                    'country': response.country.name,
                    'city': response.city.name,
                    'latitude': response.location.latitude,
                    'longitude': response.location.longitude,
                    'postal_code': response.postal.code,
                    'network': response.traits.network,
                    'user_agent': ua_string,
                    'my_cookie_value': my_cookie_value,
                    'browser':user_agent.browser.family,
                    'browser_version_string':user_agent.browser.version_string,
                    'device':user_agent.device.family,
                })

                '''
                # Збереження відвідування користувача
                save_user_visit(
                    user_ip=user_ip,
                    country=response.country.name,
                    city=response.city.name,
                    latitude=response.location.latitude,
                    longitude=response.location.longitude,
                    postal_code=response.postal.code,
                    network=response.traits.network,
                    user_agent=ua_string,
                    browser=user_agent.browser.family,
                    browser_version_string=user_agent.browser.version_string,
                    device=user_agent.device.family,
                    cookies = my_cookie_value,
                )
                '''

                # Збереження відвідування користувача
                country_name = response.country.name if response.country.name else 'Unknown'
                city_name = response.city.name if response.city.name else 'Unknown'
                latitude_value = response.location.latitude if response.location.latitude else 0.0
                longitude_value = response.location.longitude if response.location.longitude else 0.0
                postal_code_value = response.postal.code if response.postal.code else 'Unknown'
                network_value = response.traits.network if response.traits.network else 'Unknown'
                browser_family = user_agent.browser.family if user_agent.browser.family else 'Unknown'
                browser_version = user_agent.browser.version_string if user_agent.browser.version_string else 'Unknown'
                device_family = user_agent.device.family if user_agent.device.family else 'Unknown'

                save_user_visit(
                    user_ip=user_ip,
                    country=country_name,
                    city=city_name,
                    latitude=latitude_value,
                    longitude=longitude_value,
                    postal_code=postal_code_value,
                    network=network_value,
                    user_agent=ua_string,
                    browser=browser_family,
                    browser_version_string=browser_version,
                    device=device_family,
                    cookies=my_cookie_value,
                )


            except geoip2.errors.AddressNotFoundError:

                # Обробляємо випадок, коли IP-адресу не вдалося знайти в базі даних GeoIP
                context.update({
                    'user_ip': user_ip,
                    'country': None,
                    'city': None,
                    'latitude': None,
                    'longitude': None,
                    'postal_code': None,
                    'network': None,
                    'user_agent': ua_string,
                    'my_cookie_value': my_cookie_value,
                    'browser':user_agent.browser.family,
                    'browser_version_string':user_agent.browser.version_string,
                    'device':user_agent.device.family,
                })

                # Збереження відвідування користувача
                save_user_visit(

                    user_ip = user_ip,
                    country = 'Unknown',
                    city = 'Unknown',
                    latitude = 'Unknown',
                    longitude = 'Unknown',
                    postal_code = 'Unknown',
                    network = 'Unknown',
                    user_agent = ua_string,
                    browser = user_agent.browser.family,
                    browser_version_string = user_agent.browser.version_string,
                    device = user_agent.device.family,
                    cookies = my_cookie_value,

                )
        # Змінюємо значення змінної network
        settings.NETWORK = network

        return render(request, self.template_name, context)





def logout_view(request):
    logout(request)
    return redirect('index')


#"""""
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error = 'Invalid credentials. Please try again.'
                return render(request, 'login.html', {'error': error})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def web_analytics_view(request):
    # Отримуємо значення змінної NETWORK з налаштувань Django
    network = settings.NETWORK

    # Перевіряємо, чи змінна network не є None
    if network is not None:
        # Якщо є IP-адреса, виконуємо операції з GeoIP
        GEOIP_PATH = '/home/student27/CyberDefender/GeoIP/GeoLite2-ASN.mmdb'

        # Ініціалізуємо пустий список для збереження результатів
        results = []

        # Створюємо Reader об'єкт з використанням контекстного менеджера
        with geoip2.database.Reader(GEOIP_PATH) as reader:

            scan_network = ipaddress.ip_network(network)

            ip_address = network[0]
            while ip_address in scan_network:
                try:
                    response = reader.asn(ip_address)
                    response_network = response.network
                except geoip2.errors.AddressNotFoundError as e:
                    response = None
                    response_network = e.network
                results.append((response_network, response))
                ip_address = response_network[-1] + 1  # move to next subnet


        global_variable = network

        context = {
                     'results': results,
                     'global_variable':global_variable,
                  }


        # Повертаємо результати у шаблон
        return render(request, 'web_analytics.html', context)

    else:


        # Якщо network є None, повертаємо пустий шаблон або що-небудь інше
        return render(request, 'web_analytics.html')


def buttons_view(request):
    return render(request, 'buttons.html')

def cards_view(request):
    return render(request, 'cards.html')

def utilities_color_view(request):
    return render(request, 'utilities-color.html')

def utilities_border_view(request):
    return render(request, 'utilities-border.html')

def utilities_animation_view(request):
    return render(request, 'utilities-animation.html')

def utilities_other_view(request):
    return render(request, 'utilities-other.html')

def charts_view(request):
    return render(request, 'charts.html')

def tables_view(request):
    return render(request, 'tables.html')


#def get_user_ip(request):
#    user_ip = request.META.get('REMOTE_ADDR', None)
#    return HttpResponse(f"Your IP address is: {user_ip}")

#def get_user_ip(request):
#    user_ip = request.META.get('REMOTE_ADDR', None)  # Отримання IP-адреси користувача
#    return render(request, 'home.html', {'user_ip': user_ip})  # Передача IP-адреси в шаблон

