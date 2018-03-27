<template lang="html">
  <div class="g-container">
    <home-header></home-header>
    <login></login>
  </div>
</template>
<script>
import HomeHeader from '../components/header'   /* 本页面中用到了HomeHeader组件，所以就需要在这里引入一下 */
import Login from '../components/login'
export default {
  data () {
    return {
      recommends: []
    }
  },
  components: {
    HomeHeader,
    Login
  },
  created () {

  }
}
</script>

<style lang="css" scoped>

</style>
