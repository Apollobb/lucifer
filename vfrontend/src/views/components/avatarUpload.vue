<template>
    <div class="components-container">
        <pan-thumb :image="image"></pan-thumb>

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
    import {patchUser} from 'api/user';
    import store from 'store'

    export default {
        components: {ImageCropper, PanThumb},

        props: ['userinfo'],
        data() {
            return {
                imagecropperShow: false,
                imagecropperKey: 0,
                image: 'upload' + this.userinfo.avatar
            }
        },

        methods: {
            cropSuccess(resData) {
                console.log(resData);
                this.imagecropperShow = false;
                this.imagecropperKey = this.imagecropperKey + 1;
                //this.image = resData.file;
                const data = {
                    avatar: resData.filepath
                };
                patchUser(this.userinfo.id, data).then(response => {
                    if (response.statusText = 'ok') {
                        this.$message({
                            type: 'success',
                            message: '恭喜你，更新成功'
                        });
                    }
                }).catch(error => {
                    this.$message.error('更新失败');
                    console.log(error);
                });
                store.dispatch("getUserInfo");
            },
            close() {
                this.imagecropperShow = false;
            }
        }
    };
</script>

<style scoped>
</style>

