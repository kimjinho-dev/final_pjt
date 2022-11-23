<template>
  <b-container style="width: 726px">
    <h1>{{ article?.title }}</h1>
    <p>{{ article?.user }}</p>
    <img :src="`http://localhost:8000${article.image}`" alt="None" style="width:726px">
    <p>{{ article?.content }}</p>
    <span v-for="tag,index in article.tags" :key="index">#{{ tag.name }} </span>
    <br />
    <b-button @click="editState">Edit</b-button> |
    <b-button @click.prevent="deleteArticle">Delete</b-button>
  </b-container>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityDetail",
  props: {
    id: String,
  },
  data() {
    return {
      article: null,
    };
  },
  created() {
    console.log(this.id)
    this.getArticleDetail();
  },
  methods: {
    getArticleDetail() {
      axios({
        method: "get",
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
    deleteArticle() {
      axios({
        method: "DELETE",
        url: `${API_URL}/api/v1/community/${this.id}`,
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
          this.$router.go();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    editState() {
      console.log("edit Change")
      this.$emit("changeEditState")
    }
  },
};
</script>