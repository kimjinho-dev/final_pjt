<template>
  <form @submit.prevent="createArticle">
    <div>
      <label for="communityarticletitle">Title: </label>
      <input
        id="communityarticletitle"
        type="text"
        v-model.trim="communityarticletitle"
      />
      <br/>
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
      if (!this.communityarticletitle) {
        alert("제목을 입력해주세요");
        return;
      }
      axios({
        method: "POST",
        url: `${API_URL}/api/v1/community/`,
        data: {
          title: this.communityarticletitle,
          content: this.communityarticlecontent,
          tags: "#1",
        },
        headers: {
          Authorization: "Token c457306e3e505a00a28dec8bc9e3a42b736368f3",
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

<style>
</style>