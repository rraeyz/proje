"""Literatur/ETD zamanlarini BJD_TDB'ye cevirir.
Kullanim (ornek):  python zaman_donusum.py 2456000.5 HJD_UTC 97.6366450 29.6722662
"""
import sys
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation

YER_MERKEZI = EarthLocation.from_geocentric(0, 0, 0, unit=u.m)   # gozlemevi bilinmiyorsa (~20 ms hata)


def bjd_tdb(jd, sistem, ra, dec):
    """sistem: 'BJD_TDB', 'BJD_TT' (fark < 2 ms), 'BJD_UTC' ya da 'HJD_UTC'."""
    if sistem in ("BJD_TDB", "BJD_TT"):
        return jd
    if sistem == "BJD_UTC":                                        # yalniz saat cinsi farki: TDB-UTC
        return Time(jd, format="jd", scale="utc").tdb.jd
    if sistem == "HJD_UTC":                                        # gunes merkezliden Yer'e, sonra barisentre
        hedef = SkyCoord(ra, dec, unit="deg")
        t = Time(jd, format="jd", scale="utc", location=YER_MERKEZI)
        t_yer = t - t.light_travel_time(hedef, "heliocentric")
        return (t_yer.tdb + t_yer.light_travel_time(hedef, "barycentric")).jd
    raise ValueError(f"bilinmeyen zaman sistemi: {sistem} (makaleden kontrol et)")


if __name__ == "__main__":
    jd, sistem, ra, dec = float(sys.argv[1]), sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
    b = bjd_tdb(jd, sistem, ra, dec)
    print(f"{sistem} {jd:.6f} -> BJD_TDB {b:.6f}   (fark {(b - jd) * 86400:+.1f} s)")
