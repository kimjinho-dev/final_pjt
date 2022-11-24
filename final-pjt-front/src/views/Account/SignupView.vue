<template>
  <div>
    <h1>회원가입 페이지입니다</h1>
    <form @submit.prevent="signUp">
      <label for="username"></label>
      <input type="text" id="username" placeholder="아이디" v-model="username" /><br />

      <label for="password1"></label>
      <input type="password" id="password1" placeholder="비밀번호" v-model="password1" /><br />

      <label for="password2"></label>
      <input type="password" id="password2" placeholder="비밀번호 확인" v-model="password2" /><br />
      
      <input type="submit" value="SignUp" />
    </form>
  </div>
</template>

<script>
export default {
  name: "SignupView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signUp() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      };

      this.$store.dispatch("signUp", payload);
    },
  },
};
</script>

<style>
</style>