<template>
  <b-container style="width: 726px">
    <h1>Detail</h1>
    <p>{{ article?.id }}</p>
    <p>{{ article?.title }}</p>
    <p>{{ article?.content }}</p>
  </b-container>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "Detail_C_Article",
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
  },
};
</script>