<template>
  <div>
    <p>{{ article.title }}</p>
    <p>{{ article.content}}</p>
    <button @click="deleteArticle">Delete</button>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'DummyListItem',
  props: {
    article: Object,
  },
  methods: {
    deleteArticle() {
      this.$store.dispatch('deleteCommunityArticle', this.article)
    },
  }
}
</script>

<style>

</style>