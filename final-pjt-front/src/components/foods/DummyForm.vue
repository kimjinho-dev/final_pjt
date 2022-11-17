<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="foodsarticletitle">Title: </label>
      <input id="foodsarticletitle" type="text" v-model="foodsarticletitle">
    </div>
    <div>
      <label for="foodsarticlecontent">Content: </label>
      <input id="foodsarticlecontent" type="text" v-model="foodsarticlecontent">
    </div>
    <button type="submit">submit</button>
  </form>
</template>

<script>
export default {
  name: 'DummyForm',
  data() {
    return {
      foodsarticletitle: '',
      foodsarticlecontent: '',
    }
  },
  methods: {
    submitForm() {
      const data = {
        title: this.foodsarticletitle,
        content: this.foodsarticlecontent
      }
      this.$store.dispatch('createFoodsArticle', data)
    }
  },
}
</script>

<style>

</style>