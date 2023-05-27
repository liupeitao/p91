<script >
import Layout from "./Layout.vue";
import Header from "./Header.vue";
import SearchBar from "./SearchBar.vue";
export default{
  components: {
      Layout,
      SearchBar,
      Header
  }
}
</script>

<template>
  <Header></Header>
  <SearchBar></SearchBar>
  <Layout></Layout>
</template>

<style >

</style>
