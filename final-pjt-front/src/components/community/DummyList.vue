<template>
  <div>
    <DummyListItem v-for="(article, index) in communityArticles" :key="index" :article="article"/>
  </div>
</template>

<script>
import DummyListItem from '@/components/community/DummyListItem'

export default {
  name: 'DummyList',
  components: {
    DummyListItem,
  },
  computed: {
    communityArticles() {
      return this.$store.state.communityArticles
    }
  }
}
</script>

<style>

</style>