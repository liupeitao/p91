<script >
import VideoPlayer from './VideoPlayerComponents.vue'
import Favorites from './Favorites.vue'
export default {
  data() {
    return {
      id:this.infos[0],
      m3u8_url: this.infos[1],
      detail_url: this.infos[2],
      thumbnail: this.infos[3],
      duration: this.infos[4],
      title: this.infos[5],
      author: this.infos[12],
      popularites: this.infos[6],
      favorites: this.infos[7],
      comments: this.infos[8],
      likes: this.infos[9],
      dislikes: this.infos[10],
      add_time: this.infos[11]
    };
  },
  props: {
    infos: {
      type: Object,
      required: true
    }
  },
  components: {
    VideoPlayer,
    Favorites
  },
  mounted() {
  }
};


</script>

<template>
  <div el-row >
      <el-card body-style="padding: 20px" shadow="hover">
<!--        <img src="../assets/test.png" >-->
        <video-player  :video-src="m3u8_url" type="application/x-mpegURL" />
        <div style="padding: 14px;">
          <span></span>
          <div class="bottom clearfix">
<!--            <el-button type="text" class="button">{{title}}</el-button>-->
            <label>{{title}}</label> <br>
            <div style="text-align: center">
              <label>作者: {{author}}</label> <br>
              <label>时长: {{duration}}</label> <br>
              <label>热度: {{popularites}}</label> <br>
            </div>
            <favorites :prop-value="popularites"></favorites>
            <time class="time">{{add_time}}</time>
          </div>
        </div>
      </el-card>
    </div>
</template>

<style >

</style>
