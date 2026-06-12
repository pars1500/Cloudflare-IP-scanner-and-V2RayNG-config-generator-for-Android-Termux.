import urllib.request


CLOUDFLARE_IPV4_URL = "https://www.cloudflare.com/ips-v4"


def get_cloudflare_ipv4_ranges():
    try:
        request = urllib.request.Request(
            CLOUDFLARE_IPV4_URL,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response = urllib.request.urlopen(request, timeout=10)
        data = response.read().decode("utf-8")

        ranges = []

        for line in data.splitlines():
            line = line.strip()
            if line:
                ranges.append(line)

        return ranges

    except Exception as error:
        print("Error fetching Cloudflare IP ranges:", error)
        return []
