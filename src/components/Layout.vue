<script >
import Thumbnail from './Thumbnail.vue'
import axios from 'axios';
import Pagination from '../components/Pagination.vue'
import VideoPlayerComponents from "./VideoPlayerComponents.vue";
import SearchFilter from "./SearchFilter.vue";

export default {
  name : "Layout",
  components:{
    Thumbnail,
    Pagination,
    VideoPlayerComponents,
    SearchFilter
  },
  data(){
    return {
      thumbnailRows: [],
      responseData: null,
      page_size: 24,
      total: 450,
      currentPage : this.$props.page,
      keyword: '',
      chunkSize: 3
    }
  },
  props :{
    page: {
      type: Number,
      required: false
    }
  },
  computed: {
    filteredList() {
      if (this.responseData) {
        return this.chunkArray(this.responseData.filter(item => (item['author'] + item['title']).includes(this.keyword)), this.chunkSize)
      }
      return this.thumbnailRows
    },
  },

  mounted() {
   this.fetchData(this.page);
  },

  //
  // },
  methods:{
    fetchData(page) {
      axios.get(`http://10.16.23.72:5000/api/data?page=${page.toString()}&per_page=${this.page_size.toString()}`)
          .then(response => {
            this.responseData = response.data['data'];
            this.total = response.data['total']
            if (!this.thumbnailRows) {
              this.thumbnailRows = this.chunkArray(this.responseData, this.chunkSize);
            }

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
    up(value){
      this.keyword = value
    },
    // onPageSizeChange(size) {
    //   // 在这里根据新的页面大小发送请求，更新数据
    //   axios.get(`http://10.16.23.72:5000/api/pages?page=${this.currentPage}&per_page=${this.page_size}`)
    //       .then(response => {
    //         // 处理返回的数据
    //         // 更新Layout组件的数据或传递给其他组件
    //         // console.log(response.data);
    //       })
    //       .catch(error => {
    //         console.error(error);
    //       });
    // },
    onPageChange(page) {
      // 在这里根据新的当前页码发送请求，更新数据
      this.currentPage = page
      this.$props.page = page
      this.fetchData(page)
      this.$router.replace({ query: { page: page} });
      this.$emit('update:page', page);

    }
  }
}
</script>

<template>
  <div>
    <!--    <SearchFilter :infos="this.responseData" @input="up"></SearchFilter>-->
    <el-input v-model="keyword" placeholder="输入标题或者作者进行过滤" style="width: 20em; margin-bottom: 60px; border-color: #1f4029"></el-input>
  </div>
  <div>
    <el-row v-for="row in this.filteredList" :key="rowIndex" >
      <el-col v-for="thumbnail in row" :key="thumbnail.id"  :xs="24" :sm="24" :md="12" :lg="8" :xl="8">
        <div class="grid-content bg-purple">
          <Thumbnail :infos="thumbnail"></Thumbnail>
        </div>
      </el-col>
    </el-row>
  </div>

<!--  <pagination :total=200 :page_size=24 @page-click="onPageClick"></pagination>-->

  <pagination :count="this.total" :per_page="this.page_size" :current-page.sync="this.currentPage" @size-change="onPageSizeChange" @current-change="onPageChange"></pagination>
</template>

<style >
.el-row {
  margin-bottom: 4vh;
  &:last-child {
    margin-bottom: 0;
  }
}
el-col {
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
el-input{

}
</style>
