<template>
  <b-container style="width: 726px">
    <h1>{{ this.$store.state.username }} 프로필 페이지</h1>
    <hr />
    <div><UserProfile /></div>
    <hr />
    <div>
      <UserArticle />
    </div>
  </b-container>
</template>

<script>
import UserArticle from "@/components/account/UserArticle.vue";
import UserProfile from "@/components/account/UserProfile.vue";

export default {
  components: {
    UserArticle,
    UserProfile,
  },
};
</script>

<style>
</style>