<template>
  <div>
    <h1>로그인 페이지입니다.</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username" /><br />

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password" /><br />

      <input type="submit" value="logIn" />
    </form>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    logIn() {
      const username = this.username;
      const password = this.password;

      const payload = {
        username: username,
        password: password,
      };
      this.$store.dispatch("logIn", payload);
    },
  },
};
</script>

<style>
</style>