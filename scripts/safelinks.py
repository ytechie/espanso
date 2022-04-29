import sys
import urllib.parse

# espanso will pass in the clipboard contents
if len(sys.argv) > 1:
    clipboard = sys.argv[1];
else:
    clipboard = "https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fbing.com&data=foo"

parsedUrl = urllib.parse.urlparse(clipboard)
queryString = parsedUrl.query

queryParams = urllib.parse.parse_qs(queryString)

print(queryParams["url"][0])