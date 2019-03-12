<template>
  <v-app dark>
    <navbar></navbar>
    <router-view/>
  </v-app>
</template>
<style lang='scss'>
body{
  margin: 0;
  font-family: Roboto;
  .theme--dark.application{
      background: #0a0a0a;
  }
}
</style>
<script>
import navbar from '@/components/Navbar'
export default {
  name: 'App',
  components: {
    navbar
  }
}
</script>