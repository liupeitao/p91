<script >
import Layout from "./Layout.vue";
import Header from "./Header.vue";
import SearchBar from "./SearchBar.vue";
import NavMenu from "./NavMenu.vue";
export default{
  components: {
    Layout,
    SearchBar,
    Header,
    NavMenu
  },
  // watch: {
  //   page(newValue) {
  //     // 当路由参数发生变化时，更新组件状态
  //     this.page = newValue
  //   }
  // },
  data() {
    return {
      page: parseInt(this.$route.query.page) || 1
    };
  },
}
</script>

<template>
  <div>
    <Header></Header>
<!--    <SearchBar></SearchBar>-->
    <NavMenu></NavMenu>
    <Layout :page="page" ></Layout>
  </div>

</template>

<style >

</style>
