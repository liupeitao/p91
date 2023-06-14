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
  <div class="nav">
    <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#006E62"
        text-color="#FFF"
        active-text-color="#FF9000"
    >
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">性感少妇</el-menu-item>
      <el-menu-item index="3" >可爱学妹</el-menu-item>
      <el-menu-item index="4" >成熟阿姨</el-menu-item>
      <el-menu-item index="5" ><span style="font-size: 24px; font-weight: bold; color: greenyellow;">许浩文教你舔B</span> </el-menu-item>
      <el-menu-item index="6" >董事长大战曹xx</el-menu-item>
      <el-menu-item index="5" ><span style="font-size: 24px; font-weight: bold; color: lawngreen;">硕根实战教学</span> </el-menu-item>
    </el-menu>
  </div>

</template>

<style >

</style>
