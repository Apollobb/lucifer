<template>
  <div class="components-container">
    <PanThumb :avatar='avatar'>
      <p></p>
      <a class="tou">不好意思，头掉了</a>
    </PanThumb>
    <el-button type="primary" icon="upload" style="position: absolute;bottom: 15px;margin-left: 40px;" @click="imagecropperShow=true">修改头像
    </el-button>

    <ImageCropper :width="300" :height="300" url="https://httpbin.org/post" @close='close' @crop-upload-success="cropSuccess"
      :key="imagecropperKey" v-show="imagecropperShow" />
  </div>
</template>

<script>
    import ImageCropper from 'components/ImageCropper';
    import PanThumb from 'components/PanThumb';
    import {mapGetters} from 'vuex';
    export default {
      components: { ImageCropper, PanThumb },
      data() {
        return {
          imagecropperShow: false,
          imagecropperKey: 0,
        }
      },

        computed: {
            ...mapGetters([
                'avatar'
            ])
        },

      methods: {
        cropSuccess(resData) {
          this.imagecropperShow = false;
          this.imagecropperKey = this.imagecropperKey + 1;
          this.avatar = resData.files.avatar;
        },
        close() {
          this.imagecropperShow = false;
        }
      }
    };
</script>
<style scoped>
.tou {
  color: #ff363a;
}
</style>

