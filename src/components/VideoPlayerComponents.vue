<template>
  <div>
    <video ref="videoPlayer" class="video-js vjs-default-skin" controls preload="auto" width="408" height="230">
      <source :src="videoSrc" type="application/x-mpegURL">
    </video>
  </div>
</template>

<script>
import videojs from 'video.js'
import 'video.js/dist/video-js.css'
export default {
  name: 'VideoPlayer',
  props: {
    videoSrc: {
      type: String,

      required: true
    }
  },
  mounted () {
    this.player = videojs(this.$refs.videoPlayer, {}, function onPlayerReady () {
      console.log('Video.js player is ready!')
    })
  },
  beforeDestroy () {
    if (this.player) {
      this.player.dispose()
    }
  }
}
</script>

<style>
/* 在这里添加 video.js 的样式 */
</style>
