<template>
  <b-container style="width: 726px">
    <h1>Detail</h1>
    <p>{{ article?.user }}</p>
    <p>{{ article?.title }}</p>
    <p>{{ article?.content }}</p>
    <p>{{ article?.tags }}</p>
    <router-link
      :to="{ name: 'EditCommunityArticle', params: { id: article.id } }"
      >[Edit]</router-link
    >
    |
    <button @click="deleteArticle">Delete</button>
  </b-container>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityDetail",
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
        url: `${API_URL}/api/v1/community/${this.$route.params.id}`,
      })
        .then((res) => {
          console.log(res);
          this.article = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteArticle() {
      axios({
        method: "DELETE",
        url: `${API_URL}/api/v1/community/${this.$route.params.id}`,
        data: {
          title: this.communityarticletitle,
          content: this.communityarticlecontent,
          tags: this.communityarticletags,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "Community" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>