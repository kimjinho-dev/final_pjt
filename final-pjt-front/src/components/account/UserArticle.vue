<template>
  <div>
    <h3>UserArticle이 출력되는 자리입니다.</h3>
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
              <b-card-img :src="`http://localhost:8000${article.image}`" alt="None" style="width:726px" class="rounded-0"></b-card-img>
              <!-- <b-button :to="{ name: 'DetailCommunityArticle', params: { id: article.id } }">Detail</b-button> | -->
              <b-button v-b-modal.modal-1 @click="getArticleIdState(article)">Detail</b-button>
            </b-card>
          </b-card-group>
        <hr />
        </div>
      </b-container>
      <b-modal id="modal-1" title="BootstrapVue">
        <CommunityDetail v-if="state === 'Detail'" :id="this.id" @changeEditState="changeEditState" />
        <CommunityEdit v-else-if="state === 'Edit'" :id="this.id" @changeDetailState="changeDetailState" @getArticles="get_articles" />
      </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import CommunityDetail from "@/components/community/CommunityDetail.vue"
import CommunityEdit from "@/components/community/CommunityEdit";

const API_URL = "http://127.0.0.1:8000";
const DetailState = "Detail";
const EditState = "Edit";

export default {
  name: "UserArticle",

  data() {
    return {
      articles: null,
      id: null,
      state: null,
    };
  },
  components: {
    CommunityDetail,
    CommunityEdit,
    },
  methods: {
    deleteArticle() {
      this.$store.dispatch("deleteCommunityArticle", this.article);
    },
    get_articles() {
      axios({
        method: "GET",
        url: `${API_URL}/api/v3/profile/post/${this.$store.state.username}`,
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
    getArticleId(article) {
      this.id = article.id
      console.log(this.id)
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