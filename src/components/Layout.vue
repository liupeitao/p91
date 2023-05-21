<script >
import Thumbnail from './Thumbnail.vue'
import axios from 'axios';
import Pagination from '../components/Pagination.vue'
import VideoPlayerComponents from "./VideoPlayerComponents.vue";
export default {
  name : "Layout",
  components:{
    Thumbnail,
    Pagination,
    VideoPlayerComponents
  },
  data(){
    return {
      thumbnailRows: [],
      responseData: null,
      page_size: 24,
      total: 450,
      currentPage : 1
    }
  },
  mounted() {
    this.fetchData();
  },
  watch: {
    currentPage(newData) {
      // 当responseData发生变化时，重新调用fetchData()
      this.fetchData();
    }
  },
  methods:{
    fetchData() {
      axios.get(`http://10.16.23.72:5000/api/data?page=${this.currentPage.toString()}&per_page=${this.page_size.toString()}`)
          .then(response => {
            this.responseData = response.data['data'];
            const chunkSize = 3;
            this.total = response.data['total']
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
    },
    onPageSizeChange(size) {
      // 在这里根据新的页面大小发送请求，更新数据
      axios.get(`http://10.16.23.72:5000/api/pages?page=${this.currentPage}&per_page=${this.page_size}`)
          .then(response => {
            // 处理返回的数据
            // 更新Layout组件的数据或传递给其他组件
            // console.log(response.data);
          })
          .catch(error => {
            console.error(error);
          });
    },
    onPageChange(page) {
      // 在这里根据新的当前页码发送请求，更新数据
      axios.get(`http://10.16.23.72:5000/api/data?page=${page}&per_page=${this.page_size}`)
          .then(response => {
            // 处理返回的数据
            // 更新Layout组件的数据或传递给其他组件
            this.currentPage = page
            // console.log("这里是layout")
            // console.log("第" + page + "也")
            // console.log("请求的网址" + "http://127.0.0.1:5000/api/pages?page=${page}&per_page=${this.pageSize}")
            this.responseData = response.data['data']
            this.total = response.data['total']
          })
          .catch(error => {
            console.error(error);
          });
    }
  },

}

</script>

<template>
  <div>
    <el-row v-for="row in thumbnailRows" :key="rowIndex">
      <el-col v-for="thumbnail in row" :key="thumbnail.id"  :xs="24" :sm="24" :md="12" :lg="8" :xl="8">
        <div class="grid-content bg-purple">
          <Thumbnail :infos="thumbnail"></Thumbnail>
        </div>
      </el-col>
    </el-row>
  </div>

<!--  <pagination :total=200 :page_size=24 @page-click="onPageClick"></pagination>-->
  <pagination :count="this.total" :per_page="this.page_size" :current-page.sync="currentPage" @size-change="onPageSizeChange" @current-change="onPageChange"></pagination>

</template>

<style >
.el-row {
  margin-bottom: 4vh;
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
