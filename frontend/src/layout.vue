<template>
  <div class="container">
    <header>
      <slot name="header">header</slot>
    </header>
    <main>
      <slot>主要内容</slot>
    </main>
    <footer>
      <slot name="footer"><p>Copyright © 2018</p></slot>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'layout'
}
</script>

<style scoped>

</style>
