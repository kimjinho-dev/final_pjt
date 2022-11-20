<template>
  <div>
    <b-container style="width: 726px">
      <h1>Community</h1>
      <CommunitySearch />
      <router-link :to="{ name: 'CreateCommunityArticle' }">[create]</router-link>
      <hr />
      <b-container v-for="article in articles" :key="article.id">
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <p>{{ article.tags }}</p>
        <router-link
          :to="{ name: 'DetailCommunityArticle', params: { id: article.id } }"
          >[Detail]</router-link
        >
        |
        <button @click="deleteArticle">Delete</button>
      </b-container>
      <hr />
      <div v-for="article in articles" :key="article.id">
        {{article.title}}
        {{article.content}}
        {{article.tags}}
      </div>
      <CommunityList />
    </b-container>
  </div>
</template>

<script>
import CommunityList from "@/components/community/CommunityList";
import CommunitySearch from "@/components/community/CommunitySearch";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityView",

  data() {
    return {
      articles: null,
    };
  },
  components: {
    CommunityList,
    CommunitySearch,
  },
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