<template>
  <b-container style="width: 726px">
    <h1>Create Article</h1>
    <hr />
    <form @submit.prevent="createArticle" enctype=“multipart/form-data”>
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
        <br />
        <input type="file" name="image" id="image" @change="selectImage"/>
      </div>
      <button type="submit">submit</button>
    </form>
  </b-container>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityCreate",
  data() {
    return {
      communityarticletitle: null,
      communityarticlecontent: null,
      tags: null,
      image: null,
    };
  },
  methods: {
    createArticle() {
      if (!this.communityarticletitle) {
        alert("제목을 입력해주세요");
        return;
      }
      const frm = new FormData();
      frm.append("image", this.image);
      frm.append("title", this.communityarticletitle)
      frm.append("content", this.communityarticlecontent)
      frm.append("tags", this.communityarticletags)
      axios({
        method: "POST",
        url: `${API_URL}/api/v1/community/`,
        data: frm,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
          'Content-Type': 'multipart/form-data',
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
    selectImage(e) {
      this.image = e.target.files[0];
    }
  },
};
</script>

<style>
</style>