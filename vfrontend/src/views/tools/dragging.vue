<template>
    <div class="color-list">
        <div class="headerbtn">
            <el-upload
                    class="btnjson"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :on-success="handleSuccess"
                    :on-remove="handleRemove"
                    :before-upload="beforeUpload"
                    :file-list="fileList"
                    :disabled="count>0?true:false">
                <el-button v-if="count==0" type="danger">上传json</el-button>
                <el-button v-else type="info" @click="count>0?showjson=true:showjson=false">查看json</el-button>
                <a v-if="count==0" slot="tip" class="el-upload__tip tips">只能上传.json文件，且不超过500kb</a>
                <a v-else slot="tip" class="el-upload__tip tips">删除文件重新上传</a>
            </el-upload>
        </div>
        <el-row :gutter="20">
            <el-col :span="4" class="left">
                <div class="left-item">
                    <draggable v-model="jsondata" :options="{group:'people'}" @start="drag=true" @end="dragEnd">
                        <div v-for="(item, index) in jsondata">
                            <a>{{index + 1}} </a>
                            <el-badge :value="item.data" class="item">
                                <el-button class="color-item" :plain="true" type="info" size="small">{{item.name}}

                                </el-button>
                            </el-badge>
                        </div>
                    </draggable>
                </div>
            </el-col>
            <el-col :span="16" :offset="2" class="right">
                <div class="right-item">
                    <el-card class="box-card" v-for="item in jsondata" :key="item"
                             :style="{'background-color':item.color}">
                        <div slot="header" class="clearfix">
                            <span style="line-height: 12px;">{{item.name}}</span>
                        </div>
                        <div>
                            <img :src="'http://game.gtimg.cn/images/yxzj/img201606/heroimg/' + item.img + '/' + item.img + '.jpg'"
                                 class="image">
                        </div>
                    </el-card>
                </div>
            </el-col>
        </el-row>

        <el-dialog title="查看json数据" :visible.sync="showjson">
            <code>
                <pre>{{ jsonstr | prettyJson }}</pre>
            </code>
        </el-dialog>
    </div>
</template>

<script>
    import fetch from 'utils/fetch';
    import draggable from 'vuedraggable'

    export default {

        components: {
            draggable,
        },
        data() {
            return {
                showjson: false,
                jsonstr: {"data": "拖拽后生成数据"},
                fileList: [],
                jsonUrl: '',
                count: 0,
                jsondata: [],
            }
        },

        methods: {
            handleSuccess(file, fileList) {
                this.count += 1;
                this.jsonUrl = fileList.url;
                this.readJson()
            },
            handleRemove(file, fileList) {
                this.count = 0;
                this.jsondata = [];
                this.jsonstr = {"data": "拖拽后生成数据"}
            },
            beforeUpload(file) {
                const isJSON = file.name.split('.')[1] === 'json';

                if (!isJSON) {
                    this.$message.error('上传文件只能是 JSON 格式!');
                }
                return isJSON
            },
            readJson() {
                fetch({
                    url: this.jsonUrl,
                    method: 'get',
                }).then(res => {
                    let results = res.data;
                    let len = Object.keys(results).length;
                    for (var i = 1; i < len + 1; i++) {
                        this.jsondata.push(results[i]);
                    }
                });
            },
            dragEnd() {
                this.jsonstr = {};
                for (var i = 1, len = this.jsondata.length + 1; i < len; i++) {
                    this.jsonstr[i] = this.jsondata[i - 1]
                }
            }
        }
    }
</script>

<style scoped>
    .color-list {
        padding-left: 50px;
    }

    .left {
        border-radius: 5px;
        background-color: rgba(74, 255, 161, 0.58);
    }

    .left-item {
        text-align: left;
        padding: 3px 0;
    }

    .color-item {
        margin: 1px 0;
        display: inline-block;
        font-family: "arial";
    }

    .right {
        border-radius: 5px;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both;
    }

    .right-item {
        width: 750px;
    }

    .box-card {
        width: 150px;
        float: left;
    }

    .image {
        width: 100%;
        display: block;
    }

    .headerbtn {
        margin-bottom: 20px;
    }

    .btnjson {
        display: inline-block;
    }

    .tips {
        margin-left: 5px;
    }

</style>
