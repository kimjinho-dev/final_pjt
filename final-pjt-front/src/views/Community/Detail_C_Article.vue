<template>
  <b-container style="width: 726px">
    <h1>Detail</h1>
    {{article}}
    <p>{{ article?.id }}</p>
    <p>{{ article?.title }}</p>
    <p>{{ article?.content }}</p>
    <br />
    <img :src="`http://localhost:8000${article.image}`" alt="None" style="width:726px">
    {{article.id}}
    <button @click="deleteArticle(article.id)">delete</button>
  </b-container>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "Detail_C_Article",
  props:{
    id: String
  },
  data() {
    return {
      article: null,
    };
  },
  created() {
    this.getArticleDetail();
  },
  methods: {
    getArticleDetail() {
      axios({
        method: "get",
        // url: `${API_URL}/api/v1/community/${this.$route.params.id}`,
        url: `${API_URL}/api/v1/community/${this.id}`,
      })
        .then((res) => {
          console.log(res);
          this.article = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteArticle(id) {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/community/${id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.$router.push({name:'Community'})
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>