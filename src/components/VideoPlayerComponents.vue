<template>
  <div>
    <video ref="videoPlayer" class="video-js vjs-default-skin" controls preload="auto" width="1240" height="700" >
      <source :src="videoSrc" >
<!--      type="application/x-mpegURL"-->
    </video>
  </div>
</template>

<script>
import videojs from 'video.js'
import 'video.js/dist/video-js.css'
export default {
  name: 'VideoPlayer',
  // props: {
  //   videoSrc: this.$route.query.url
  // },
  mounted () {
    this.player = videojs(this.$refs.videoPlayer, {}, function onPlayerReady () {
      console.log('Video.js player is ready!')
    })
  },
  data(){
    return {
      videoSrc: this.$route.query.url
    }
  },
  beforeDestroy () {
    if (this.player) {
      console.log("player 死亡了")
      this.player.dispose()
    }
    console.log("player 死亡了")
  }
}
</script>

<style>
/* 在手机上，将视频宽度设置为100% */


/* 在这里添加 video.js 的样式 */
</style>
