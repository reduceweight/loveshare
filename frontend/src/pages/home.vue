<template lang="html">
  <div class="g-container">
    <home-header></home-header>
  </div>
</template>
<script>
import HomeHeader from '../components/header'   /* 本页面中用到了HomeHeader组件，所以就需要在这里引入一下 */
export default {
  data () {
    return {
      recommends: []
    }
  },
  components: {
    HomeHeader
  },
  created () {

  }
}
</script>

<style lang="css" scoped>

</style>
