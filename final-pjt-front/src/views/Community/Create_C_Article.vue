<template>
  <form @submit.prevent="createArticle">
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
    </div>
    <button type="submit">submit</button>
  </form>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "Create_C_Article",
  data() {
    return {
      communityarticletitle: null,
      communityarticlecontent: null,
    };
  },
  methods: {
    createArticle() {
      const data = {
        title: this.communityarticletitle,
        content: this.communityarticlecontent,
      };
      if (!data.title) {
        alert("제목을 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/community/`,
        data: {
          title: data.title,
          content: data.content,
          tags: "#1",
        },
        headers: {
          Authorization: `Token df16842a90f1d9aea223e8b9cb93156ab06cc528`,
        },
      })
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "ArticleView" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
</style>