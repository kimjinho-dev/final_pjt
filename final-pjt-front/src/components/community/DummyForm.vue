<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="communityarticletitle">Title: </label>
      <input id="communityarticletitle" type="text" v-model="communityarticletitle">
      <br>
      <textarea cols="30" rows="10" v-model="communityarticlecontent"></textarea>
    </div>
    <button type="submit">submit</button>
  </form>
</template>

<script>
export default {
  name: 'DummyForm',
  data() {
    return {
      communityarticletitle: '',
      communityarticlecontent: '',
    }
  },
  methods: {
    submitForm() {
      const data = {
        title: this.communityarticletitle,
        content: this.communityarticlecontent
      }
      this.$store.dispatch('createCommunityArticle', data)
    }
  },
}
</script>

<style>

</style>