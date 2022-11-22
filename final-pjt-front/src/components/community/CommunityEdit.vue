<template>
  <b-container style="width: 726px">
    <h1>Edit Article</h1>
    <hr />
    <form @submit.prevent="editArticle">
      <div>
        <label for="communityarticletitle">Title: </label>
        <input
          id="communityarticletitle"
          type="text"
          v-model.trim="communityarticletitle"
        />
        <br />
        <textarea
          cols="30"
          rows="10"
          v-model="communityarticlecontent"
        ></textarea>
        <br />
        <label for="communityarticletags">Tags: </label>
        <input
          id="communityarticletags"
          placeholder="#태그1 #태그2"
          type="text"
          v-model.trim="communityarticletags"
        />
      </div>
      <b-button type="submit">submit</b-button>
    </form>
  </b-container>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityEdit",
  props: {
    id: String,
  },
  data() {
    return {
      communityarticletitle: null,
      communityarticlecontent: null,
      tags: null,
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
    editArticle() {
      if (!this.communityarticletitle) {
        alert("제목을 입력해주세요");
        return;
      }
      axios({
        method: "PUT",
        url: `${API_URL}/api/v1/community/${this.id}/`,
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
          this.$emit("changeDetailState")
        })
        .catch((err) => {
          console.log(err);
        });
      }
    }
}
</script>

<style>
</style>