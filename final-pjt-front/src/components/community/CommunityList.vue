<template>
  <div>
    <CommunityListItem
      v-for="(article, index) in communityArticles"
      :key="index"
      :article="article"
    />
  </div>
</template>

<script>
import CommunityListItem from "@/components/community/CommunityListItem";

export default {
  name: "CommunityList",
  components: {
    CommunityListItem,
  },
  computed: {
    communityArticles() {
      return this.$store.state.communityArticles;
    },
  },
};
</script>

<style>
</style>