<template>
  <div>
    <h3>UserArticle이 출력되는 자리입니다.</h3>
    <div v-for="article in articles" :key="article.id">
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
      <p>{{ article.tags }}</p>
      <router-link
        :to="{ name: 'DetailCommunityArticle', params: { id: article.id } }"
        >[Detail]</router-link
      >
      |
      <button @click="deleteArticle">Delete</button>
      <hr />
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "UserArticle",

  data() {
    return {
      articles: null,
    };
  },
  components: {},
  methods: {
    deleteArticle() {
      this.$store.dispatch("deleteCommunityArticle", this.article);
    },
    get_articles() {
      axios({
        method: "GET",
        url: `${API_URL}/api/v1/community/`,
      })
        .then((res) => {
          console.log(res);
          this.articles = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.get_articles();
  },
};
</script>

<style>
</style>