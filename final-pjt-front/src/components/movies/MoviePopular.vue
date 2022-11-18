<template>
  <div>
    <h1>MoviePopular</h1>
    <VueSlickCarousel v-bind="settings">
      <div v-for="image in tempdata" :key="image.id">
        <b-img thumbnail fluid :src="`${image.src}`" @click="moveDetail(image.id)"></b-img>
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
        {id:671, src:'https://image.tmdb.org/t/p/w500/unEtC8uWn2lcQLnwKG9PZJX0h0c.jpg	'},
        {id:672, src:'https://image.tmdb.org/t/p/w500/sfs4U6XpiKFngbbSzrpZbkM1ySI.jpg '},
        {id:674, src:'https://image.tmdb.org/t/p/w500/h6BhNwNXg0IEbs2PoWfCX9QEvgl.jpg	'},
        {id:767, src:'https://image.tmdb.org/t/p/w500/fHfnrfpQXt91XN4XBh9DMDFuYdq.jpg	'},
      ],
    }
  },
  components: { 
    VueSlickCarousel, 
  },
  methods: {
    moveDetail(id) {
      this.$router.push({name: 'movieDetail', params:{movie_id:id}})
    },
  }
}
</script>

<style>

</style>