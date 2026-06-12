import socket
import time

PORTS = [443, 2053, 2083, 2087, 2096, 8443]


def test_ip(ip, timeout=2):
    results = []

    for port in PORTS:
        try:
            start = time.time()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)

            result = sock.connect_ex((ip, port))

            latency = int((time.time() - start) * 1000)

            sock.close()

            if result == 0:
                results.append({
                    "ip": ip,
                    "port": port,
                    "latency": latency
                })

        except:
            pass

    return results
