<script >
export default {
  data() {
    return {
      value: 3.5
    }
  }
}
</script>

<template>
  <el-rate
      v-model="value"
      disabled
      show-score
      text-color="#ff9900"
      score-template="{value}">
  </el-rate>
  <br>

</template>

<style >

</style>
