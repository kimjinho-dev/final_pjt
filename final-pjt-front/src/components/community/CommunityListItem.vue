<template>
  <div>
    <p>{{ article.id }}</p>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <router-link
      :to="{ name: 'DetailCommunityArticle', params: { id: article.id } }"
      >[Detail]</router-link
    >
    |
    <button @click="deleteArticle">Delete</button>
    <hr />
  </div>
</template>

<script>
export default {
  name: "CommunityListItem",
  props: {
    article: Object,
  },
  methods: {
    deleteArticle() {
      this.$store.dispatch("deleteCommunityArticle", this.article);
    },
  },
};
</script>

<style>
</style>