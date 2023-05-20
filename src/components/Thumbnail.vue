<script >
import VideoPlayer from './VideoPlayerComponents.vue'
import Favorites from './Favorites.vue'
export default {

  data(){

  },
  components: {
    VideoPlayer,
    Favorites
  },
}

</script>

<template>
  <div el-row >
      <el-card body-style="padding: 20px" shadow="hover">
<!--        <img src="../assets/test.png" >-->
        <video-player  video-src="https://la3.killcovid2021.com/m3u8/823536/823536.m3u8" type="application/x-mpegURL" />
        <div style="padding: 14px;">
          <span></span>
          <div class="bottom clearfix">
            <el-button type="text" class="button">商场试衣间口爆刚成年18岁小女友</el-button>
            <br>
            <favorites></favorites>
            <time class="time">2023-05-20</time>
          </div>
        </div>
      </el-card>
    </div>
</template>

<style >

</style>
