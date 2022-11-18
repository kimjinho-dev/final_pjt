<template>
  <div>
    <h1>MovieRandomGenre</h1>
    <VueSlickCarousel v-bind="settings">
      <div v-for="image in tempdata" :key="image.id">
        <b-img thumbnail fluid :src="`${image.src}`"></b-img>
      </div>
    </VueSlickCarousel>
  </div>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  data() {
    return {
      settings: {
        "dots": false,
        "infinite": false,
        "initialSlide": 2,
        "speed": 500,
        "slidesToShow": 3,
        "slidesToScroll": 1,
        "swipeToSlide": true
      },
      tempdata: [
        {id:1, src:'https://img1.daumcdn.net/thumb/C300x430/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4127deb531fea9b766461efb61da18af55697d3c'},
        {id:2, src:'https://an2-img.amz.wtchn.net/image/v2/nV_paIE6IwxSBGsVh1DbGw.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk56STVlREV3T0RCeE9EQWlYU3dpY0NJNklpOTJNaTl6ZEc5eVpTOXBiV0ZuWlM4eE5qTTBPRGd4TWpnMk5UazFOams1T0RFeEluMC5vaXhoNTVPTHhzcVZIeEdiUUNaVjFOSUdNRXhpTDFOR3FHM0E1RXFCLXNR'},
        {id:3, src:'https://an2-img.amz.wtchn.net/image/v2/tMV4xweIwBYwOmYwBwJwvg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk56STVlREV3T0RCeE9EQWlYU3dpY0NJNklpOTJNaTl6ZEc5eVpTOXBiV0ZuWlM4eE5qTXhNek16TkRrek5EY3dORFF5TnpjNEluMC5IQUtCYUVEQ2FsX0FvbHIxU1dMVFdDeC1pbkJWakd0RDZaYXZteHJMYXZF'},
        {id:4, src:'https://an2-img.amz.wtchn.net/image/v2/9tjaINfC3poXuaW3vIA11w.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk56STVlREV3T0RCeE9EQWlYU3dpY0NJNklpOTJNaTl6ZEc5eVpTOXBiV0ZuWlM4eE5qTXhNek15T1RZek5URTFNREkyT0RRMUluMC5DR1dsaGdQWlVZWkl0UFFERF9WbWFaUTFpQ1lkMkFvaVpya1JOX1U0UHpV'},
      ],
    }
  },
  components: { 
    VueSlickCarousel, 
  },
}
</script>

<style>

</style>