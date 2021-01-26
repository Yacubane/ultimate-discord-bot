from urllib.parse import urlencode
from urllib.request import Request, urlopen
import re
import json
import urllib


def run_code(args):
    regex = r"\+run\s*```\s*([\s\S]*)```\s*"
    matches = re.finditer(regex, args.content, re.MULTILINE)
    code = ""
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            code = match.group(groupNum + 1)
            break
        break

    url = 'https://pynative.com/editor.php'
    post_fields = {"data": '{"source_code":"' + code + '","language_id":10,"stdin":""}'}
    parsed_data = urllib.parse.urlencode(post_fields)\
        .replace("%0A", "%5Cn")\
        .replace("%28", "(") \
        .replace("%29", ")") \
        .encode()
    request = Request(
        url,
        parsed_data,
        headers={
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                          "AppleWebKit/536.5 (KHTML, like Gecko) "
                          "Chrome/19.0.1084.52 Safari/536.5"
        }
    )
    response = urlopen(request).read().decode()
    if response == "Server error":
        return "Jakiś syntax error ziomeczku"
    data = json.loads(response)
    if "stderr" in data and data["stderr"]:
        return data["stderr"]
    if "error" in data and data["error"]:
        return data["error"]
    return data["stdout"]

