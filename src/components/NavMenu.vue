<script >
export default {
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<template>
  <el-menu
    :default-active="activeIndex2"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#006E62"
    text-color="#FFF"
    active-text-color="#ffd04b">
    <el-menu-item index="1">首页</el-menu-item>
    <el-menu-item index="2">性感少妇</el-menu-item>
<!--    <el-submenu index="2">-->
<!--      <template slot="title">性感少妇</template>-->
<!--      <el-menu-item index="2-1">选项1</el-menu-item>-->
<!--      <el-menu-item index="2-2">选项2</el-menu-item>-->
<!--      <el-menu-item index="2-3">选项3</el-menu-item>-->
<!--      <el-submenu index="2-4">-->
<!--        <template slot="title">可爱学妹</template>-->
<!--        <el-menu-item index="2-4-1">选项1</el-menu-item>-->
<!--        <el-menu-item index="2-4-2">选项2</el-menu-item>-->
<!--        <el-menu-item index="2-4-3">选项3</el-menu-item>-->
<!--      </el-submenu>-->
<!--    </el-submenu>-->
    <el-menu-item index="3" >可爱学妹</el-menu-item>
<!--    <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">成熟阿姨</a></el-menu-item>-->
    <el-menu-item index="4" >成熟阿姨</el-menu-item>
    <el-menu-item index="5" >许浩文教你添b</el-menu-item>
    <el-menu-item index="6" >董事长大战曹xx</el-menu-item>
  </el-menu>
</template>

<style >

</style>
