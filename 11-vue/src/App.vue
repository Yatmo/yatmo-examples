<script setup lang="ts">
import { YatmoMap, YatmoNeighbourhoodText, YatmoPois } from '@yatmo/vue';

// Your Yatmo FRONTEND key (the one locked to your domains): VITE_YATMO_KEY in a .env file.
const KEY = import.meta.env.VITE_YATMO_KEY ?? 'YOUR_FRONTEND_KEY';

// Stand-in for a listing from your API.
const listing = {
  title: 'Bright 2-bedroom flat, Rue de la Loi, Brussels',
  price: '€ 395 000',
  facts: ['Flat · 92 m² · 2 bedrooms', 'Floor 2 / 5, lift', 'EPC B', 'Charges € 140 / month'],
  description: 'Second floor, south-facing living room, fully equipped kitchen, two bedrooms, cellar and bicycle storage. Free of occupation.',
  latitude: 50.8461,
  longitude: 4.3664,
};

const yatmo = { key: KEY, country: 'BE' as const, language: 'EN' as const, latitude: listing.latitude, longitude: listing.longitude };
</script>

<template>
  <main>
    <header>
      <h1>{{ listing.title }}</h1>
      <p class="price">{{ listing.price }}</p>
    </header>

    <div class="listing">
      <div>
        <div class="gallery">Photo gallery</div>
        <h2>Description</h2>
        <p>{{ listing.description }}</p>
      </div>
      <aside class="facts">
        <ul><li v-for="f in listing.facts" :key="f">{{ f }}</li></ul>
        <a class="cta" href="#contact">Book a visit</a>
      </aside>
    </div>

    <section>
      <h2>Neighbourhood</h2>
      <!-- The interactive map: points of interest, travel times, summary over the map, 5/10/20 minute areas. -->
      <YatmoMap :license-key="KEY" country="BE" language="EN" :latitude="listing.latitude" :longitude="listing.longitude"
                marker="circle" :circle-radius-in-meters="300" isochrone="right" :rounded="12" :height="520" />
    </section>

    <div class="columns">
      <section>
        <h2>Around the property</h2>
        <!-- Nearest places by category, walking times. -->
        <YatmoPois :client="yatmo" :categories="['education', 'shopping', 'transport']">
          <template #fallback><p>Loading places…</p></template>
        </YatmoPois>
      </section>
      <section>
        <h2>Living here</h2>
        <!-- The neighbourhood text. With Nuxt, pass `text` from @yatmo/sdk on the server instead, so search engines index it. -->
        <YatmoNeighbourhoodText :client="yatmo" titles="city">
          <template #fallback><p>Loading the neighbourhood text…</p></template>
        </YatmoNeighbourhoodText>
      </section>
    </div>
  </main>
</template>
