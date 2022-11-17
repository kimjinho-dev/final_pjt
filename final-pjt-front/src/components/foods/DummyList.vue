<template>
  <div>
    <DummyListItem v-for="(article, index) in foodsArticles" :key="index" :article="article"/>
  </div>
</template>

<script>
import DummyListItem from '@/components/foods/DummyListItem'

export default {
  name: 'DummyList',
  components: {
    DummyListItem,
  },
  computed: {
    foodsArticles() {
      return this.$store.state.foodsArticles
    }
  }
}
</script>

<style>

</style>