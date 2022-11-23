<template>
  <div>
    <b-container style="width: 726px">
      <h1>Community</h1>
      <CommunitySearch />
      <b-button v-b-modal.modal-1>Create</b-button>
      <hr />
      <h1>{{$route.params.searchData}} 태그로 검색된 결과</h1>
      <b-container v-if="articles.length < 1">
        <h2>검색한 데이터 값이 없습니다</h2>
      </b-container>
      <b-container v-else v-for="article in articles" :key="article.id">
        <div>
          <b-card-group deck>
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
              <b-card-img v-if="`${article.image}`" :src="`http://localhost:8000${article.image}`" alt="None" class="rounded-0"></b-card-img>
              <b-button v-b-modal.modal-2 @click="getArticleIdState(article)">Detail</b-button>
            </b-card>
          </b-card-group>
        <hr />
        </div>
      </b-container>
    </b-container>
    <b-modal id="modal-1" title="Bootstrapvue">
      <CommunityCreate />
    </b-modal>
    <b-modal id="modal-2" title="BootstrapVue" hide-footer>
      <CommunityDetail v-if="state === 'Detail'" :id="this.id" @changeEditState="changeEditState" />
      <CommunityEdit v-else-if="state === 'Edit'" :id="this.id" @changeDetailState="changeDetailState"/>
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
      articles: [],
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
      axios({
        method: "GET",
        url: `${API_URL}/api/v1/community/tag/${this.$route.params.searchData}/`,
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
  watch: {
    '$route' () {
      this.get_articles();
    }
  }
};
</script>