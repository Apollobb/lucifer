<template>
    <div class="color-list">
        <div class="headerbtn">
            <el-upload
                    class="uploadjson"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :on-success="handleSuccess"
                    :on-remove="handleRemove"
                    :file-list="fileList"
                    :disabled="count>0?true:false">
                <el-button v-if="count==0" type="danger">上传json</el-button>
                <el-button v-else class="showjson" type="info"
                           @click="count>0?dialogJsonVisible=true:dialogJsonVisible=false">查看json
                </el-button>
                <a v-if="count==0" slot="tip" class="el-upload__tip">只能上传.json文件，且不超过500kb</a>
                <a v-else slot="tip" class="el-upload__tip">删除文件重新上传</a>
            </el-upload>
        </div>
        <el-row :gutter="20">
            <el-col :span="4" class="left">
                <div
                        class="left-item"
                        v-for="(item,index) in jsondata"
                        v-dragging="{ item: item, list: jsondata, group: 'item'}"
                        :key="item.name"
                >
                    <a>{{index + 1}}、</a>
                    <el-button class="color-item">{{item.name}}</el-button>
                </div>
            </el-col>
            <el-col :span="16" :offset="2" class="right">
                <div class="right-item">
                    <el-card class="box-card" v-for="item in jsondata" :key="item"
                             :style="{'background-color':item.color}">
                        <div slot="header" class="clearfix">
                            <span style="line-height: 12px;">{{item.name}}</span>
                        </div>
                        <div class="text item">
                            <ul>
                                <li>{{item.data}}</li>
                                <li>{{item.color}}</li>
                                <li>{{item.like}}</li>
                            </ul>
                        </div>
                    </el-card>
                </div>
            </el-col>
        </el-row>

        <el-dialog title="查看json数据" :visible.sync="dialogJsonVisible">
            <code>
                <pre>{{ jsonstr | prettyJson }}</pre>
            </code>
        </el-dialog>
    </div>
</template>

<script>
    import fetch from 'utils/fetch';

    export default {
        data() {
            return {
                dialogJsonVisible: false,
                jsonstr: {"data": "没有数据"},
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
                this.jsonUrl = '';
            },
            readJson() {
                fetch({
                    url: this.jsonUrl,
                    method: 'get',
                }).then(res => {
                    let results = res.data;
                    let len = Object.keys(results).length;
                    for (var i = 0; i < len; i++) {
                        this.jsondata.push(results[i]);
                    }
                });
            }
        },
        mounted() {
            this.$dragging.$on('dragged', ({value}) => {
                let results = value.list;
                this.jsonstr = {};
                for (var i = 0, len = results.length; i < len; i++) {
                    this.jsonstr[i] = results[i]
                }
            });
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

    .headerbtn {
        margin-bottom: 20px;
    }

    .showjson {
        display: inline-block;
    }

    .uploadjson {
        display: inline-block;
    }

</style>
