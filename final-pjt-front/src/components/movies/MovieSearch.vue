<template>
  <div>
    <h1>영화검색</h1>
    <b-form-input 
      id="type-search"   
      :type="type"    
      v-model="searchData"
      placeholder="검색할 영화를 입력해주세요"
      @keyup.enter="search(searchData)"  
      ></b-form-input>
      searchData:{{searchData}}
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
    search() {

    }
  },
}
</script>

<style>

</style>