# 12. Webflow (and Wix, Squarespace, Framer): no backend, no developer

A property page the way a no-code builder produces it: the Yatmo map, the nearest places and the neighbourhood
text come from three HTML snippets fed by an **address** (the only thing a CMS usually holds), through the
`@yatmo/elements` web components. `index.html` is the published result; the two snippets below are what you paste.

Full tutorial with screenshots and an embed code generator: [documentation.yatmo.com/plugins/webflow](https://documentation.yatmo.com/plugins/webflow).

## Site-wide code (Webflow: Site settings > Custom code > Head code)

```html
<script type="module" src="https://cdn.jsdelivr.net/npm/@yatmo/elements@1/dist/yatmo-elements.js"></script>
<yatmo-config key="YOUR_FRONTEND_KEY" country="BE" language="EN"></yatmo-config>
```

## Embed elements on the Properties Template page

```html
<yatmo-map address="ADDRESS_FROM_CMS" marker="circle" circle-radius="300" isochrone="right" rounded="12" height="520"></yatmo-map>

<yatmo-pois address="ADDRESS_FROM_CMS" categories="education,transport,shopping" mode="walking"></yatmo-pois>

<yatmo-text address="ADDRESS_FROM_CMS" heading="h3" titles="street-city"></yatmo-text>
```

In the Webflow embed editor, select `ADDRESS_FROM_CMS`, click **+ Add Field** and pick the Address field of the
collection. With coordinates instead: `latitude="..." longitude="..."` and two Number fields. The address is looked
up by Yatmo once per page, shared by the three elements.

## Style

The elements render plain `h3`, `p` and `ul` inside the page, so your site's CSS applies; `index.html` shows the few
rules used for the grid of places.
