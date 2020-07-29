import pygeoip
from requests import get

def get_geolocation():
    """
    This function gets the geolocation based in external ip
    """
    ip = get('https://api.ipify.org').text

    gip = pygeoip.GeoIP('./data/GeoLiteCity.dat')
    res = gip.record_by_addr(ip)

    return res