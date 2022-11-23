<template>
  <div id="moviedetail">
    <b-container style="width:726px">
      <b-card no-body class="overflow-hidden" style="max-width: 726px; background-color:#E0E7E9; color:#000">
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" alt="Image" class="rounded-0"></b-card-img>
          </b-col>
          <b-col md="6" align-self="start" style="word-break: keep-all;">
            <b-card-body :title="`${movie?.title}`">
              <p>줄거리 : </p>
              <b-card-text style="font-size:0.8em;background-color:#354649;color:#E0E7E9;">
                <p v-if="movie.overview">{{ movie?.overview }}</p>
                <p v-else>줄거리가 없습니다...</p>
              </b-card-text>
              <p>장르 : </p>
              <b-card-text style="background-color:#354649 ;color:#E0E7E9;">
                <span v-for="genre in movie?.genre_ids" :key="genre.id"><span>{{genre.name}}</span>&nbsp;</span>
              </b-card-text>
              <b-card-text>
                <p>평점 : {{ movie?.vote_average }}</p>
                <span class='star-rating' style="width: ;">
                <span :style ="`width: ${ratingToPercent()}%`"></span>
                </span>
              </b-card-text>
              <b-card-text>
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
    },
    ratingToPercent() {
      const score = this.movie.vote_average * 10;
      return score
    },
  }
}
</script>

<style>
#moviedetail {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align:start;
  color: #fff ;
  background-color: #6C7A89;
}

/* .star-ratings {
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent;
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
} */


.star-rating { width:300px; }
.star-rating,.star-rating span { display:inline-block; height:55px; overflow:hidden; background:url(star.png)no-repeat; }
.star-rating span{ background-position:left bottom; line-height:0; vertical-align:top; }



</style>