import ipaddress
from urllib.parse import urlparse

SHORTENERS = {
    "bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "ow.ly"
}

def analyze_url(url):
    if url.startswith("www."):
        url = "http://" + url

    parsed = urlparse(url)
    host = parsed.hostname or ""
    warnings = []

    if parsed.scheme != "https":
        warnings.append("URL does not use HTTPS.")

    try:
        ipaddress.ip_address(host)
        warnings.append("URL uses an IP address instead of a normal domain.")
    except ValueError:
        pass

    if "@" in parsed.netloc:
        warnings.append("URL contains '@', which can be misleading.")

    if "xn--" in host:
        warnings.append("Domain contains punycode.")

    if host in SHORTENERS:
        warnings.append("URL uses a link-shortening service; verify the destination.")

    if len(url) > 150:
        warnings.append("URL is unusually long.")

    return warnings
