<script>
export default {
  props: {
    propValue: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      value: ((5 * this.propValue)/(148000)).toFixed(1)
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
