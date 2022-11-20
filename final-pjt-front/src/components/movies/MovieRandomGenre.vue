<template>
  <div>
    <h1>MovieRandomGenre</h1>
    <div v-for="(movies,index) in three_movies" :key="index">
      <h1>{{genres[index]}} 장르추천</h1>
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
      three_movies: [],
      genres: [],
    }
  },
  components: { 
    VueSlickCarousel, 
  },
  methods: {
    moveDetail(id) {
      this.$router.push({name: 'movieDetail', params:{movie_id:id}})
    },
    getRandomGenreMovieList() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movies/movie_random_genre/`
      })
        .then((res) => {
          this.three_movies = res.data.slice(0,3)
          this.genres = res.data[3]
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getRandomGenreMovieList()
  }
}
</script>

<style>

</style>