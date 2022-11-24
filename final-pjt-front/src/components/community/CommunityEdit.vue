<template>
  <b-container style="width: 726px; ">
    <h1>Edit Article</h1>
    <hr />
    <form @submit.prevent="editArticle">
      <div>
        <label for="communityarticletitle"></label>
        <input
          id="communityarticletitle"
          type="text"
          placeholder="제목"
          v-model.trim="communityarticletitle"
        />
        <br />
        <textarea
          cols="30"
          rows="10"
          placeholder="내용"
          v-model="communityarticlecontent"
        ></textarea>
        <br />
        <label for="communityarticletags"></label>
        <input
          id="communityarticletags"
          placeholder="#태그1 #태그2"
          type="text"
          v-model.trim="communityarticletags"
        />
        <br />
        <input type="file" name="image" id="image" @change="selectImage"/>
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
      image: null,
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
      const frm = new FormData();
      frm.append("image", this.image);
      frm.append("title", this.communityarticletitle)
      frm.append("content", this.communityarticlecontent)
      frm.append("tags", this.communityarticletags)
      axios({
        method: "PUT",
        url: `${API_URL}/api/v1/community/${this.id}/`,
        data: frm,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
          'Content-Type': 'multipart/form-data',
        },
      })
        .then((res) => {
          console.log(res);
          console.log("created")
          this.$emit("getArticles")
          console.log("changeDetail")
          this.$emit("changeDetailState")
        })
        .catch((err) => {
          console.log(err);
        });
      },
      selectImage(e) {
        this.image = e.target.files[0];
      }
    }
}
</script>

<style>
.modal-body {
   background-color: #6C7A89;
   border-radius: 5px;
}
</style>