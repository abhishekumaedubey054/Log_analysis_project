import random
from datetime import datetime, timedelta

ips = [f"192.168.1.{i}" for i in range(1, 11)]
methods = ["GET", "POST", "DELETE", "PUT"]
urls = ["/home", "/login", "/dashboard", "/api/data", "/contact"]
statuses = [200, 201, 301, 400, 403, 404, 500, 502, 503]

with open("data/access_log.txt", "w") as f:
    for _ in range(100):
        ip = random.choice(ips)
        dt = (datetime.now() - timedelta(minutes=random.randint(0, 1000))).strftime("%d/%b/%Y:%H:%M:%S +0000")
        method = random.choice(methods)
        url = random.choice(urls)
        status = random.choice(statuses)
        size = random.randint(100, 5000)
        f.write(f'{ip} - - [{dt}] "{method} {url} HTTP/1.1" {status} {size}\n')
