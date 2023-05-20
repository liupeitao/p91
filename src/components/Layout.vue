<script >
import Thumbnail from './Thumbnail.vue'
import axios from 'axios';

export default {
  name : "Layout",
  components:{
    Thumbnail
  },
  data(){
    return {
      responseData: null
    }
  },
  mounted() {
    this.fetchData();
  },
  methods:{
    fetchData() {
      axios.get('https://api.example.com/data')
          .then(response => {
            this.responseData = response.data;
          })
          .catch(error => {
            console.error(error);
          });
    }
  }

}

</script>

<template>
  <el-row>
    <el-col :span="8"><div class="grid-content bg-purple"><Thumbnail></Thumbnail></div></el-col>
    <el-col :span="8"><div class="grid-content bg-purple-light"><Thumbnail></Thumbnail> </div></el-col>
    <el-col :span="8"><div class="grid-content bg-purple"><Thumbnail></Thumbnail></div></el-col>
  </el-row>

  <el-row>
    <el-col :span="8"><div class="grid-content bg-purple"><Thumbnail></Thumbnail></div></el-col>
    <el-col :span="8"><div class="grid-content bg-purple-light"><Thumbnail></Thumbnail></div></el-col>
    <el-col :span="8"><div class="grid-content bg-purple"><Thumbnail></Thumbnail></div></el-col>
  </el-row>

</template>

<style >
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
