<template>
    <div class="components-container">
        <pan-thumb :image='image'></pan-thumb>

        <el-button class="upload" type="primary" icon="upload"
                   style="position: absolute;bottom: 15px;margin-left: 40px;"
                   @click="imagecropperShow=true">修改头像
        </el-button>


        <image-cropper :width="300" :height="300" url="https://httpbin.org/post" @close='close'
                       @crop-upload-success="cropSuccess" :key="imagecropperKey"
                       v-show="imagecropperShow"></image-cropper>
    </div>
</template>

<script>
    import ImageCropper from 'components/ImageCropper';
    import PanThumb from 'components/PanThumb';
    import {mapGetters} from 'vuex';

    export default {
        components: {ImageCropper, PanThumb},
        data() {
            return {
                imagecropperShow: false,
                imagecropperKey: 0,
                image: 'https://wpimg.wallstcn.com/577965b9-bb9e-4e02-9f0c-095b41417191'
            }
        },
        computed: {
            ...mapGetters(['avatar'])
        },
        methods: {
            cropSuccess(resData) {
                this.imagecropperShow = false;
                this.imagecropperKey = this.imagecropperKey + 1;
                this.image = resData.files.avatar;
            },
            close() {
                this.imagecropperShow = false;
            }
        }
    };
</script>

<style scoped>
</style>

