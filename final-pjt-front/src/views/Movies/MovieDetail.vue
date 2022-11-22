<template>
  <div>
    <b-container style="width:726px">

      <b-card no-body class="overflow-hidden" style="max-width: 726px;">
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" alt="Image" class="rounded-0"></b-card-img>
          </b-col>
          <b-col md="6" align-self="start">
            <b-card-body :title="`${movie?.title}`">
              <b-card-text>
                <p>줄거리 : {{ movie?.overview }}</p>
                <p>
                  장르 : <span v-for="genre in movie?.genre_ids" 
                  :key="genre.id">
                  {{genre.name}}
                  </span>
                </p>
                  <p>평점 : {{ movie?.vote_average }}</p>
                  <p>개봉일자 : {{ movie?.release_date }}</p>                
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
    </b-card>
    <br />
      <h1>#{{movie?.title}}로 작성된 게시물</h1>      
      <div v-for="article in article_tag" :key="article.id">
        <p>작성자 : {{article.username}}</p>
        <p>글제목 : {{article.title}}</p>
        <p>글내용 : {{article.content}}</p>
        <p>
          태그 : <span v-for="tag,index in article.tags" :key="index">#{{ tag.name }} </span>
        </p>        
        <img :src="`http://localhost:8000${article.image}`" alt="None" style="width:300px">
        <hr>
      </div>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  data() {
    return {
      movie: null,
      article_tag: null,
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
          this.getArticleTag()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getArticleTag() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/tag/${this.movie.title}/`
      })
        .then((res) => {
          console.log(res)
          this.article_tag = res.data
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