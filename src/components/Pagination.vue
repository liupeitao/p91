<script>
import axios from 'axios';
export default {
  data(){
      return {
        // page_size: this.per_page,
        // total: this.count,
        currentPage: 1,
    }
  },
  props: {
    per_page: {
      type: Number,
      required: true
    },
    count: {
      type: Number,
      required: true
    }
  },
  methods: {
    handleSizeChange(val) {
      this.per_page = val;
      this.$emit('size-change', val); // 触发自定义的size-change事件，将新的页面大小传递给父组件

      // 发送请求
      // this.fetchData();
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.$emit('current-change', val); // 触发自定义的current-change事件，将新的当前页码传递给父组件

      // 发送请求
      // this.fetchData();
      console.log(`当前页: ${val}`);
    },
    // fetchData() {
    //   // 在这里根据新的页面大小和当前页码发送请求，更新数据
    //   // 使用axios或其他方式发送请求，获取数据
    //   axios.get(`http://127.0.0.1:5000/api/data?page=${this.currentPage}&per_page=${this.page_size}`)
    //       .then(response => {
    //         // 处理返回的数据
    //         // 更新组件的数据或传递给其他组件
    //         console.log(response.data);
    //       })
    //       .catch(error => {
    //         console.error(error);
    //       });
    // }
  },
}
</script>

<template>
  <div class="pagination-container">
    <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-size="this.per_page"
        layout="prev, pager, next, jumper"
        :total="this.count">
    </el-pagination>
  </div>
</template>

<style>
.pagination-container {
  margin-top: 15vh;
  margin-bottom: 15vh;

  display: flex;
  justify-content: center;
}
</style>
