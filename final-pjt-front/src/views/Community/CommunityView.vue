<template>
  <div>
    <h1>Community</h1>
    <router-link :to="{ name: 'CreateCommunityArticle' }">[create]</router-link>
    <hr />
    <CommunityList />
  </div>
</template>

<script>
import CommunityList from "@/components/community/CommunityList";

export default {
  name: "CommunityView",
  components: {
    CommunityList,
  },
};
</script>