<template>
  <div class="search-container">
    <el-input
        v-model="searchText"
        placeholder="搜索全站资源"
        suffix-icon="el-icon-search"
        @keydown.enter="handleSearch"
    ></el-input>
    <el-button color="#006E62" @click="handleSearch">搜索</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchText: ''
    };
  },
  methods: {
    handleSearch() {
      // 处理搜索逻辑，例如向后端发送搜索请求
      console.log('搜索:', this.searchText);
    }
  }
};
</script>

<style >
.search-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 12vh;
}
.search-container .el-input {
  margin-right: 10px;
  max-width: 300px;
}
</style>
