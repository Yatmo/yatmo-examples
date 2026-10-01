#!/usr/bin/env sh
# The nearest places by category around a property, with distances and travel times.
# https://documentation.yatmo.com/api/endpoints/summary
: "${YATMO_KEY:?set YATMO_KEY to your backend key}"

curl -sS -H "LicenseKey: $YATMO_KEY" \
  'https://be.yatmo.com/summary?latitude=50.8461&longitude=4.3664&language=EN'
