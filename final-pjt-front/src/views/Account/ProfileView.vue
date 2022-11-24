<template>
  <b-container style="width: 726px">
    <h1>{{ this.$store.state.username }}'s Articles</h1>
    <hr />
    <div>
      <UserArticle />
    </div>
  </b-container>
</template>

<script>
import UserArticle from "@/components/account/UserArticle.vue";

export default {
  components: {
    UserArticle,
  },
};
</script>

<style>
</style>