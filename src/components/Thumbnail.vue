<script >
import VideoPlayer from './VideoPlayerComponents.vue'
import Favorites from './Favorites.vue'
export default {
  data() {
    return {
      isHovered: false,
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
  },
  methods: {
    highlightCard(isHovered) {
      const cardElement = document.getElementById('card');
      if (isHovered) {
        cardElement.style.border = '2px solid #ff9900';
      } else {
        cardElement.style.border = 'none';
      }
    }
  }
};


</script>

<template>
  <div el-row  >
      <el-card id="card" body-style="padding: 20px" shadow="hover" :class="{ 'highlighted': isHovered }" @mouseover="isHovered = true" @mouseout="isHovered = false" >
<!--        <img src="../assets/test.png" >-->
        <video-player  :video-src="m3u8_url" type="application/x-mpegURL" />
        <div style="padding: 20px;">
          <span></span>
          <div class="bottom clearfix">
<!--            <el-button type="text" class="button">{{title}}</el-button>-->
            <label>{{title}}</label> <br>
            <div  style="text-align: center">
              <el-tag type="success">作者:{{author}}</el-tag> <br>
<!--              <label>作者: {{author}}</label> <br>-->
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
.highlighted {
  border: 4px solid;
  border-image:linear-gradient(to right, rgb(67, 198, 172), rgb(248, 255, 174));
  //border-image: linear-gradient(to right, rgb(103, 178, 111), rgb(76, 162, 205));
  border-image-slice: 1;
  transform: scale(1.1);
  background: linear-gradient(to right, rgb(190, 147, 197), rgb(123, 198, 204));
  //background: linear-gradient(to right, rgb(31, 64, 55), rgb(153, 242, 200));
  //background: linear-gradient(to right, rgb(31, 64, 55), rgb(153, 242, 200));
  //background: linear-gradient(to right, rgb(103, 178, 111), rgb(76, 205, 171));
}
</style>
