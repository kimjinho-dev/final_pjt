<template>
  <div>
    <b-container style="width: 726px">
      <h1>Community</h1>
      <CommunitySearch />
      <router-link :to="{ name: 'CreateCommunityArticle' }"
        >[create]</router-link
      >
      <hr />
      <b-container v-for="article in articles" :key="article.id">
        <div>
          <b-card-group deck>
            <!-- <span v-for="tag in article.tags" :key="tag.id">#{{ tag.name }} </span> -->
            <b-card
              header-tag="header"
              footer="tags"
              footer-tag="footer"
              :title="getTitle(article)"
            >
              <b-card-text>{{ article.content }}</b-card-text>
              <b-button :to="{ name: 'DetailCommunityArticle', params: { id: article.id } }">Detail</b-button> |
              <b-button v-b-modal.modal-1>Detail</b-button>
            </b-card>
          </b-card-group>
        <hr />
        </div>
      </b-container>
    </b-container>
    <b-modal id="modal-1" title="BootstrapVue">
    </b-modal>
  </div>
</template>

<script>
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
    CommunitySearch,
  },
  methods: {
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
    getTitle(article) {
      return article.title
    },
  },
  created() {
    this.get_articles();
  },
};
</script>