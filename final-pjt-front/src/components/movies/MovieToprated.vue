<template>
  <div>
    <h1>MovieToprated</h1>
    <VueSlickCarousel v-bind="settings" v-if="movies.length">
      <div v-for="movie in movies" :key="movie.id">
        <b-img thumbnail
        height="300px" width="200px"
        :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" 
        @click="moveDetail(movie.id)">
      </b-img>
      </div>
    </VueSlickCarousel>
  </div>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  data() {
    return {
      settings: {
        "dots": false,
        "focusOnSelect": true,
        "infinite": false,
        "speed": 500,
        "slidesToShow": 3,
        "slidesToScroll": 3,
        "touchThreshold": 5
      },
      movies: [],
    }
  },
  components: { 
    VueSlickCarousel, 
  },
  methods: {
    moveDetail(id) {
      this.$router.push({name: 'movieDetail', params:{movie_id:id}})
    },
    getTopratedMovieList() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movies/toprated/`
      })
        .then((res) => {
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getTopratedMovieList()
  }
}
</script>

<style>
.slick-prev:before, .slick-next:before { 
    color:rgb(7, 7, 7) !important;
}
</style>