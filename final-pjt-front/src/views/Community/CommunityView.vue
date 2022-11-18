<template>
  <div>
    <h1>Community</h1>
    <router-link :to="{ name: 'CreateCommunityArticle' }">[create]</router-link>
    <hr />
    <div v-for="article in articles" :key="article.id">
      {{article.title}}
      {{article.content}}
      {{article.tags}}
    </div>
    <CommunityList />
  </div>
</template>

<script>
import CommunityList from "@/components/community/CommunityList";
import axios from "axios"
const API_URL = "http://127.0.0.1:8000"

export default {
  name: "CommunityView",
  data() {
    return {
      articles:null,
    }
  },
  components: {
    CommunityList,
  },
  methods: {
    get_articles() {
      axios({
        method: "GET",
        url: `${API_URL}/api/v1/community/`,
      })
        .then((res) => {
          console.log(res);
          this.articles = res.data
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.get_articles()
  }
};
</script>