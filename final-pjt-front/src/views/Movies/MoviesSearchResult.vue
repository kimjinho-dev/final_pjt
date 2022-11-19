<template>
  <div>
    <b-container style="width:726px">
      <MovieSearch/>
      <h1>{{this.$route.params.searchData}} 검색결과</h1>
      <hr>
      <b-card-group deck>
        <div v-for="movie in movies" :key="movie.id">
          <b-card  
          :img-src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" 
          @click="moveDetail(movie.id)" 
          img-alt="Image"
          style="width: 200px;height: 400px;" 
          img-top
          class="mb-4">
            <b-card-text >{{movie.title}}</b-card-text>
          </b-card>        
        </div>
      </b-card-group>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import MovieSearch from '@/components/movies/MovieSearch'

export default {
  components: {
    MovieSearch,
  },
  data() {
    return {
      movies: [],
    }
  },
  methods: {
    getMovieList() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movies/search/${this.$route.params.searchData}/`
      })
        .then((res) => {
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    moveDetail(id) {
      this.$router.push({name: 'movieDetail', params:{movie_id:id}})
    },
  },
  created() {
    this.getMovieList()
  },
  watch: {
    '$route' () {
      this.getMovieList()
    }
  }
}
</script>

<style>

</style>