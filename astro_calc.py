
import swisseph as swe
import pytz
from datetime import datetime
from geopy.geocoders import Nominatim

swe.set_ephe_path('.')

def get_coordinates(place):
    geo = Nominatim(user_agent="astro_app")
    loc = geo.geocode(place)
    return (loc.latitude, loc.longitude) if loc else (0.0, 0.0)

def calculate_positions(date_str, time_str, place):
    dt = datetime.strptime(date_str + " " + time_str, "%d.%m.%Y %H:%M")
    tz = pytz.timezone("Europe/Prague")
    ut = tz.localize(dt).astimezone(pytz.utc)
    jd = swe.julday(ut.year, ut.month, ut.day, ut.hour + ut.minute / 60.0)

    lat, lon = get_coordinates(place)
    sun = swe.calc_ut(jd, swe.SUN)[0][0]
    moon = swe.calc_ut(jd, swe.MOON)[0][0]
    asc = swe.houses(jd, lat, lon)[0][0]

    sun_sign = int(sun // 30)
    moon_sign = int(moon // 30)
    asc_sign = int(asc // 30)

    zodiac = ["Beran", "Býk", "Blíženci", "Rak", "Lev", "Panna", "Váhy", "Štír", "Střelec", "Kozoroh", "Vodnář", "Ryby"]
    return zodiac[sun_sign], zodiac[moon_sign], zodiac[asc_sign]
