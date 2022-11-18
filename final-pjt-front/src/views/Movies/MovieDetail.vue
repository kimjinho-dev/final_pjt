<template>
  <div>
    <h1>movieDetail</h1>
    <p>영화제목 : {{ movie?.title }}</p>
    <p>줄거리 : {{ movie?.overview }}</p>
    <p>포스터 : 
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="">
    </p>
    <p>평점 : {{ movie?.vote_average }}</p>
    <p>개봉일자 : {{ movie?.release_data }}</p>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  data() {
    return {
      movie: null,
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movies/${this.$route.params.movie_id}/`
      })
        .then((res) => {
          console.log(res)
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>