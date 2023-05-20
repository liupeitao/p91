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
      thumbnailRows: [],
      responseData: null,
    }
  },
  mounted() {
    this.fetchData();
  },
  methods:{
    fetchData() {
      axios.get('http://127.0.0.1:5000/api/data')
          .then(response => {
            this.responseData = response.data;
            console.log(this.responseData)
            const chunkSize = 3;
            this.thumbnailRows = this.chunkArray(this.responseData, chunkSize);
          })
          .catch(error => {
            console.error(error);
          });


    },
    chunkArray(array, size) {
      const result = [];
      for (let i = 0; i < array.length; i += size) {
        result.push(array.slice(i, i + size));
      }
      return result;
    }
  },

}

</script>

<template>
<!--  <el-row>-->
<!--    <el-col :span="8"><div class="grid-content bg-purple"><Thumbnail></Thumbnail></div></el-col>-->
<!--    <el-col :span="8"><div class="grid-content bg-purple-light"><Thumbnail></Thumbnail> </div></el-col>-->
<!--    <el-col :span="8"><div class="grid-content bg-purple"><Thumbnail></Thumbnail></div></el-col>-->
<!--  </el-row>-->

<!--  <el-row>-->
<!--    <el-col :span="8"><div class="grid-content bg-purple"><Thumbnail></Thumbnail></div></el-col>-->
<!--    <el-col :span="8"><div class="grid-content bg-purple-light"><Thumbnail></Thumbnail></div></el-col>-->
<!--    <el-col :span="8"><div class="grid-content bg-purple"><Thumbnail></Thumbnail></div></el-col>-->
<!--  </el-row>-->

  <div>
    <el-row v-for="row in thumbnailRows" :key="rowIndex">
      <el-col v-for="thumbnail in row" :key="thumbnail.id" :span="8">
        <div class="grid-content bg-purple">
          <Thumbnail :infos="thumbnail"></Thumbnail>
        </div>
      </el-col>
    </el-row>
  </div>

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
