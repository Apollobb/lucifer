<template>
    <div class="color-list">
        <el-button class="showjson" type="info" @click="dialogJsonVisible=true">json数据</el-button>
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
                <el-card class="box-card" v-for="item in jsondata" :key="item" :style="{'background-color':item.color}">
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
    import ElButton from "../../../node_modules/element-ui/packages/button/src/button.vue";
    import ElInput from "../../../node_modules/element-ui/packages/input/src/input.vue";

    export default {
        components: {
            ElInput,
            ElButton
        },
        data() {
            return {
                dialogJsonVisible: false,
                jsonstr: {"data": "没有数据"},
                jsondata: [{
                    name: "aaa",
                    color: "#FF88C2",
                    data: "1991",
                    like: "打球"
                }, {
                    name: "bbb",
                    color: "#33FFAA",
                    data: "1992",
                    like: "游戏"
                }, {
                    name: "ccc",
                    color: "#FFFF33",
                    data: "1993",
                    like: "唱歌"
                }, {
                    name: "ddd",
                    color: "#99FF33",
                    data: "1994",
                    like: "跳舞"
                }, {
                    name: "eee",
                    color: "#5555FF",
                    data: "1921",
                    like: "游泳"
                }, {
                    name: "rrr",
                    color: "#9955FF",
                    data: "1931",
                    like: "跑步"
                }, {
                    name: "ttt",
                    color: "#FF3EFF",
                    data: "5634",
                    like: "旅行"
                }, {
                    name: "fff",
                    color: "#E63F00",
                    data: "99841",
                    like: "吃饭"
                }, {
                    name: "ggg",
                    color: "#00AA88",
                    data: "1313",
                    like: "电影"
                },
                ]
            }
        },

        mounted() {
            this.$dragging.$on('dragged', ({value}) => {
                const results = value.list;
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
        background-color: rgba(255, 233, 23, 0.29);
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both;
    }

    .box-card {
        width: 150px;
        float: left;
    }

    .showjson {
        margin-bottom: 20px;
    }
</style>
