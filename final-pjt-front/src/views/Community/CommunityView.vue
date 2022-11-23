<template>
  <div>
    <b-container style="width: 726px">
      <h1>Community</h1>
      <CommunitySearch />
      <b-button v-b-modal.modal-1>Create</b-button>
      <hr />
      <b-container v-for="article in articles" :key="article.id" style="color:black;text-align: start;">
        <div>
          <b-card-group deck>
            <b-card
              header-tag="header"
              footer-tag="footer"
            >
              <template #header>
                <span style="font-size:1.4em;">{{article.title}}</span>
              </template>
              <b-card-text>
                {{ article.content }}
                <br />
                <b-button v-b-modal.modal-2 @click="getArticleIdState(article)">Detail</b-button>
                <br />
              </b-card-text>
              <b-card-img :src="`http://localhost:8000${article.image}`" fluid-glow alt="None" style="object-fit:cover" class="rounded-0"></b-card-img>
              <template #footer>
                <span v-for="tag,index in article.tags" :key="index">#{{ tag.name }} </span>
              </template>
            </b-card>
          </b-card-group>
        <hr />
        </div>
      </b-container>
    </b-container>
    <b-modal id="modal-1" title="Bootstrapvue" hide-header hide-footer>
      <CommunityCreate />
    </b-modal>
    <b-modal id="modal-2" size="lg" title="BootstrapVue" hide-header hide-footer>
      <CommunityDetail v-if="state === 'Detail'" :id="this.id" @changeEditState="changeEditState" />
      <CommunityEdit v-else-if="state === 'Edit'" :id="this.id" @changeDetailState="changeDetailState" @getArticles="get_articles" />
    </b-modal>
  </div>
</template>

<script>
import CommunitySearch from "@/components/community/CommunitySearch";
import CommunityDetail from "@/components/community/CommunityDetail";
import CommunityEdit from "@/components/community/CommunityEdit";
import CommunityCreate from "@/components/community/CommunityCreate";

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
    CommunityCreate
  },
  methods: {
    get_articles() {
      console.log("get_articles")
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

<style>
</style>