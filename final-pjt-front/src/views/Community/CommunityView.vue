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
            <b-card-img :src="`http://localhost:8000${article.image}`" alt="None" style="width:726px" class="rounded-0"></b-card-img>
            <b-card
              header-tag="header"
              footer="tags"
              footer-tag="footer"
              :title="getTitle(article)"
            >
              <b-card-text>
                {{ article.content }}
                <span v-for="tag,index in article.tags" :key="index">#{{ tag.name }} </span>
              </b-card-text>
              <!-- <b-button :to="{ name: 'DetailCommunityArticle', params: { id: article.id } }">Detail</b-button> | -->
              <b-button v-b-modal.modal-1 @click="getArticleIdState(article)">Detail</b-button>
            </b-card>
          </b-card-group>
        <hr />
        </div>
      </b-container>
    </b-container>
    <b-modal id="modal-1" title="BootstrapVue" hide-footer>
      <CommunityDetail v-if="state === 'Detail'" :id="this.id" @changeEditState="changeEditState" />
      <CommunityEdit v-else-if="state === 'Edit'" :id="this.id" @changeDetailState="changeDetailState"/>
    </b-modal>
  </div>
</template>

<script>
import CommunitySearch from "@/components/community/CommunitySearch";
import CommunityDetail from "@/components/community/CommunityDetail";
import CommunityEdit from "@/components/community/CommunityEdit";
// import DetailCommunityArticle from "@/views/Community/Detail_C_Article"

import axios from "axios";

const API_URL = "http://127.0.0.1:8000";
const DetailState = "Detail";
const EditState = "Edit";

export default {
  name: "CommunityView",

  data() {
    return {
      articles: null,
      id: null,
      state: null,
    };
  },
  components: {
    CommunitySearch,
    CommunityDetail,
    CommunityEdit,
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
    getArticleIdState(article) {
      this.id = article.id
      this.state = DetailState
    },
    changeEditState() {
      this.state = EditState
      console.log(this.state)
    },
    changeDetailState() {
      this.state = DetailState
    }
  },
  created() {
    this.get_articles();
  },
};
</script>