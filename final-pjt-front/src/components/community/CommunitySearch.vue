<template>
  <div>
    <h1>게시글 검색</h1>
    <b-form-input
      v-model="searchData"
      placeholder="검색할 태그를 입력해주세요"
      @keyup.enter="search(searchData)"
    ></b-form-input>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchData: null,
    };
  },
  methods: {
    search(searchData) {
      this.$router.push({name: 'CommunitySearchResult', params:{searchData:searchData}})
    },
  },
};
</script>

<style>
</style>