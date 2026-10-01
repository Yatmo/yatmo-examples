// The neighbourhood text and the nearest places from a server, with @yatmo/sdk (backend key).
//   export YATMO_KEY=your_backend_key && npm install && npm run text
import { createYatmoClient, renderSummaryText } from '@yatmo/sdk';

const yatmo = createYatmoClient({ key: process.env.YATMO_KEY, country: 'BE', language: 'EN' });
const flat = { latitude: 50.8461, longitude: 4.3664 };

// 1. The text as HTML, ready to write into a property page (cache it: a location rarely changes).
const text = await yatmo.summaryText(flat);
console.log(renderSummaryText(text, { heading: 'h3', titles: 'street-city' }));

// 2. The nearest places with walking times, for a facts table.
const summary = await yatmo.summary(flat);
for (const category of summary.categories) {
  for (const sub of category.subCategories) {
    const place = sub.places[0];
    const walk = place?.travelData.find((t) => t.travelMode === 'walking');
    if (place) console.log(`${sub.singularLabel ?? sub.label}: ${place.name} (${walk?.travelTimeShortLabel ?? '?'} on foot)`);
  }
}
