<template>
  <div>
    <b-form-input 
      v-model="searchData"
      placeholder="검색할 영화를 입력해주세요"
      @keyup.enter="movieSearch(searchData)"  
      ></b-form-input>
      <br>
  </div>
</template>

<script>

export default {
  data() {
    return {
      searchData:null,
    }
  },
  methods: {
    movieSearch(searchData) {
      this.$router.push({name: 'searchresult', params:{searchData:searchData}})
    }
  },
}
</script>

<style>

</style>