# REST API from your server

The API is for server-to-server calls with your **backend** key, sent in the `LicenseKey` header. Use it to write
the neighbourhood text into your pages at render time (indexable), to enrich listings in your database, or to
build your own widgets. Full reference: [documentation.yatmo.com/api](https://documentation.yatmo.com/api).

The host is the country sub-domain: `be.yatmo.com`, `fr.yatmo.com`, `uk.yatmo.com`...
([countries](https://documentation.yatmo.com/countries)).

| Script | What it does |
|---|---|
| `summary.sh` | The nearest places by category with travel times, as JSON (`/summary`) |
| `summary_text.py` | The neighbourhood text in every language of the country, printed as HTML (`/Summary/text`) |

```bash
export YATMO_KEY=your_backend_key
./summary.sh
python3 summary_text.py
```
