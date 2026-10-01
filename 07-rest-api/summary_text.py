"""The neighbourhood text of a property, rendered as HTML headings and paragraphs.

One call returns every language of the country; pick the one of your page. Cache the answer
(a location rarely changes) and write the HTML into the page on the server, so search engines
index it. https://documentation.yatmo.com/api/endpoints/summary
"""
import html
import json
import os
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

KEY = os.environ.get("YATMO_KEY") or sys.exit("set YATMO_KEY to your backend key")
COUNTRY, LANGUAGE = "be", "EN"
LATITUDE, LONGITUDE = 50.8461, 4.3664

url = f"https://{COUNTRY}.yatmo.com/Summary/text?" + urlencode({"latitude": LATITUDE, "longitude": LONGITUDE})
with urlopen(Request(url, headers={"LicenseKey": KEY})) as response:
    summary = json.load(response)

for index, paragraph in enumerate(summary["Paragraphs"]):
    language = LANGUAGE if paragraph["Title"].get(LANGUAGE) else "EN"
    # First heading with the street, second with the city, the others generic.
    title_key = "TitleBis" if index == 0 and paragraph.get("TitleBis") else "TitleTer" if index == 1 and paragraph.get("TitleTer") else "Title"
    sentences = [s[language] for s in paragraph.get("Sentences", []) if s.get(language)]
    if not sentences:
        continue
    print(f"<h3>{html.escape(paragraph[title_key][language])}</h3>")
    text = html.escape(" ".join(sentences)).replace("[STRONG]", "<strong>").replace("[/STRONG]", "</strong>")
    print(f"<p>{text}</p>")
