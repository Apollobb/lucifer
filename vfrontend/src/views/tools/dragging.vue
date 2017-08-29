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
                            <el-badge :value="item.category" class="item">
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
                            <img :src="'http://172.16.31.202:1702/images/dtgames/h/' + item.pic" class="image">
                        </div>
                    </el-card>
                </div>
            </el-col>
        </el-row>

        <el-dialog title="查看json数据" :visible.sync="showjson">
            <code>
                <pre>{{ jsondata }}</pre>
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
                fileList: [],
                jsonUrl: '',
                count: 0,
                jsondata: [
                    {
                        "eName": "Saiyan Battle",
                        "name": "赛亚烈战",
                        "id": "dragonball",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "dragonball.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "Nightclub",
                        "name": "夜店之王",
                        "id": "nightclub5x20",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": "1",
                        "language": "zh_CN",
                        "pic": "nightclub5x20.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "Basketball Master",
                        "name": "灌篮大师",
                        "id": "sd",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "sd.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "Investiture of Gods",
                        "name": "封神榜",
                        "id": "tlod",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "tlod.png",
                        "tag": [
                            "HOT",
                            "NEW",
                            "BFA"
                        ]
                    },
                    {
                        "eName": "whitesnake",
                        "name": "白蛇传",
                        "id": "whitesnake",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "whitesnake.png",
                        "tag": [
                            "HOT",
                            "NEW",
                            "CT"
                        ]
                    },
                    {
                        "eName": "Glory of Heroes",
                        "name": "英雄荣耀",
                        "id": "crystal",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": "1",
                        "language": "zh_CN",
                        "pic": "crystal.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "casino ",
                        "name": "3D老虎机",
                        "id": "casino",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": "1",
                        "language": "zh_CN",
                        "pic": "casino.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "Seiya",
                        "name": "圣域传说",
                        "id": "seiya",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "seiya.png",
                        "tag": [
                            "HOT",
                            "NEW",
                            "CT"
                        ]
                    },
                    {
                        "eName": "Fourss",
                        "name": "四圣兽",
                        "id": "fourss",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": "1",
                        "language": "zh_CN",
                        "pic": "fourss.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "Crazy Basketball",
                        "name": "劲爆篮球",
                        "id": "btball5x20",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "20-25",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "btball5x20.png",
                        "tag": [
                            "HOT",
                            "NEW",
                            "BFA"
                        ]
                    },
                    {
                        "eName": "KING OF PIRATE",
                        "name": "海盗无双",
                        "id": "onepiece",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "onepiece.png",
                        "tag": [
                            "HOT",
                            "NEW",
                            "CT"
                        ]
                    },
                    {
                        "eName": "Wealthy God Arriving",
                        "name": "财神到",
                        "id": "tgow",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "tgow.png",
                        "tag": [
                            "NEW",
                            "HOT"
                        ]
                    },
                    {
                        "eName": "Naruto",
                        "name": "NINJA",
                        "id": "naruto",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "naruto.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "DragonPhoenix Prosper",
                        "name": "龙凤呈祥",
                        "id": "dnp",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "15-20",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "dnp.png",
                        "tag": [
                            "HOT",
                            "NEW",
                            "BFA"
                        ]
                    },
                    {
                        "eName": "Xiyouji",
                        "name": "西游记",
                        "id": "xiyouji5x25",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "xiyouji5x25.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "Tales Of Wusong",
                        "name": "武松传",
                        "id": "watermargin",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "watermargin.png",
                        "tag": [
                            "HOT",
                            "NEW",
                            "CT"
                        ]
                    },
                    {
                        "eName": "Allah Lamp",
                        "name": "阿拉丁神灯",
                        "id": "aladdin5x243",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "aladdin5x243.png",
                        "tag": [
                            "HOT",
                            "NEW",
                            "CT"
                        ]
                    },
                    {
                        "eName": "Chinese Paladin",
                        "name": "仙剑奇缘",
                        "id": "xjqy5x9",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": "1",
                        "language": "zh_CN",
                        "pic": "xjqy5x9.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "FULUSHOU",
                        "name": "福禄寿",
                        "id": "fls",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": "1",
                        "language": "zh_CN",
                        "pic": "fls.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "Demon Hunt to West",
                        "name": "西游降妖",
                        "id": "jtw",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "jtw.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "crazy5x243",
                        "name": "疯狂转转转",
                        "id": "crazy5x243",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "DEM",
                        "line": " ",
                        "state": "DEM",
                        "language": "zh_CN",
                        "pic": "crazy5x243.png",
                        "jackpot": 1,
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "Happy New Year",
                        "name": "新年到",
                        "id": "newyear",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "newyear.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    },
                    {
                        "eName": "Basketball Master 2",
                        "name": "灌篮大师2",
                        "id": "sd5",
                        "category": "DT",
                        "subType": "DT-2",
                        "type": "SLO",
                        "line": "",
                        "state": 1,
                        "language": "zh_CN",
                        "pic": "sd5.png",
                        "tag": [
                            "HOT",
                            "NEW"
                        ]
                    }
                ]
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
                    this.jsondata = res.data;
                });
            },
            dragEnd() {
                console.log(this.jsondata)
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
