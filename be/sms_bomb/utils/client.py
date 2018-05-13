import requests

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sms_bomb.settings")
django.setup()

from servers.models import Server

default_headers = {
    "Accept":"application/json, text/plain, */*",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    "Content-Type":"application/json;charset=UTF-8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9"
}

def request(url, method="GET", headers="{}", content=None, phone = "13207638353"):
    if type(headers) == str:
        headers = eval(headers)
    headers = default_headers.update(headers)
    r = requests.request(url=url, headers=headers, method=method, data=content.replace("$<phone>",phone))
    return r.text


if __name__ == "__main__":
    server = Server.objects.get(id=1)

    r = request(url=server.url, headers=server.headers, method=server.method, content=server.content)
    if server.response in r:
        server.success_times = server.success_times + 1
    else:
        server.failed_times = server.failed_times + 1
        server.last_fail = r
    print(r)