<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'Movies' }">Movies</router-link> |
      <router-link :to="{ name: 'Community' }">Community</router-link> |
      <router-link
        v-if="this.$store.getters.getUserToken === null"
        :to="{ name: 'Signup' }"
        >Signup</router-link
      >
      <router-link v-else :to="{ name: 'Profile' }">Profile</router-link>
      |
      <router-link
        v-if="this.$store.getters.getUserToken === null"
        :to="{ name: 'Login' }"
        >Login</router-link
      >
      <button v-else @click="logout">Logout</button>
      <p>환영합니다 {{ this.$store.getters.getUserName }}</p>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.dispatch("logOut");
    },
  },
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
