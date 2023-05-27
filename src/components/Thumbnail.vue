<script >
import VideoPlayer from './VideoPlayerComponents.vue'
import Favorites from './Favorites.vue'
import moment from "moment";

export default {
  data() {
    return {
      isHovered: false,
      id:this.infos['id'],
      m3u8_url: this.infos['m3u8_url'],
      detail_url: this.infos['detail_url'],
      thumbnail: this.infos['thumbnail'],
      duration: this.infos['duration'],
      title: this.infos['title'],
      author: this.infos['author'],
      popularites: this.infos['popularites'],
      favorites: this.infos['favorites'],
      comments: this.infos['comments'],
      likes: this.infos['likes'],
      dislikes: this.infos['dislikes'],
      add_time: this.infos['add_time']
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
    },
    play( url ){
        this.$router.push(`/play?url=${url}`)
    }
  },
  computed: {
    updateTime() {
      const currentTime = moment();
      const addTime = moment(this.add_time, 'ddd, DD MMM YYYY HH:mm:ss Z');
      const diffInSeconds = currentTime.diff(addTime, 'seconds');
      // 根据差值进行格式化
      if (diffInSeconds < 60) {
        return `${diffInSeconds} 秒前`;
      } else if (diffInSeconds < 3600) {
        const diffInMinutes = Math.floor(diffInSeconds / 60);
        return `${diffInMinutes} 分钟前`;
      } else if (diffInSeconds < 86400) {
        const diffInHours = Math.floor(diffInSeconds / 3600);
        return `${diffInHours} 小时前`;
      } else {
        const diffInDays = Math.floor(diffInSeconds / 86400);
        return `${diffInDays} 天前`;
      }
    },
  },
  watch: {

  },
};


</script>

<template>
      <el-card id="card" body-style="padding: 20px" shadow="hover" :class="{ 'highlighted': isHovered }" @mouseover="isHovered = true" @mouseout="isHovered = false" @click="play(m3u8_url)">
        <img :src="thumbnail"  alt="x">
        <div style="padding: 15px;">
          <div class="bottom clearfix">
            <label>{{title}}</label> <br>
            <el-tag type="info" color="#B7E1A7">{{updateTime}}更新</el-tag> <br>
            <div  style="text-align: center">
              <el-tag type="success">作者:{{author}}</el-tag> <br>
              <el-tag type="info" >热度: {{popularites}}</el-tag> <br>
<!--              <label>热度: {{popularites}}</label> <br>-->
              <favorites :prop-value="popularites"></favorites>
              <label>时长: {{duration}}</label> <br>
              <time class="time">{{add_time}}</time>
            </div>
          </div>
        </div>
      </el-card>
</template>

<style >
.highlighted {
  border: 4px solid;
  border-image:linear-gradient(to right, rgb(67, 198, 172), rgb(248, 255, 174));
  //border-image: linear-gradient(to right, rgb(103, 178, 111), rgb(76, 162, 205));
  transform: scale(1.1);
  background: linear-gradient(to right, rgb(190, 147, 197), rgb(123, 198, 204));
  //background: linear-gradient(to right, rgb(31, 64, 55), rgb(153, 242, 200));
  //background: linear-gradient(to right, rgb(31, 64, 55), rgb(153, 242, 200));
  //background: linear-gradient(to right, rgb(103, 178, 111), rgb(76, 205, 171));
}
</style>
