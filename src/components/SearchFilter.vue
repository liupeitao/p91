<script>
export default {
  data() {
    return {
      restaurants: [],
      state1: '',
      state2: ''
    };
  },
  props : {
    infos :{
      type: Object,
      required: true
    }
  },
  methods: {
    querySearch(queryString, cb) {
      var restaurants = this.restaurants;
      var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
      // 调用 callback 返回建议列表的数据
      cb(results);
      this.$emit("input", queryString)
    },
    createFilter(queryString) {
      return (restaurant) => {
        return (restaurant.value.toLowerCase().includes(queryString.toLowerCase()));
      };

    },

    loadAll() {
      // return this.$props.infos
      let lists = []
      for (let info of this.$props.infos) {
          let dict = {
            "value": info['title'],
            "address": info['author'],
          }
          lists.push(dict)
      }
      return lists
    },
    handleSelect(item) {
      this.$emit("input", this.state1)
    }
  },
  mounted() {
    this.restaurants = this.loadAll();
  }
}
</script>

<template>
  <el-col :span="12">
    <div class="sub-title">激活即列出输入建议</div>
    <el-autocomplete
        class="inline-input"
        v-model="state1"
        :fetch-suggestions="querySearch"
        placeholder="请输入内容"
        @select="handleSelect"
    ></el-autocomplete>
    <el-button color="#006E62" @click="handleSearch">搜索</el-button>
  </el-col>
</template>
<style scoped>

</style>
