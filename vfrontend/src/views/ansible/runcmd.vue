<template xmlns="http://www.w3.org/1999/html">
    <el-card class="runcmd">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <div>
                <sesect-hosts :selecthost="ruleForm.hosts" @gethosts="getHosts"></sesect-hosts>
            </div>
            <el-form-item label="执行命令" prop="cmd">
                <el-input v-model="ruleForm.cmd"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="postForm('ruleForm')">执行</el-button>
            </el-form-item>
        </el-form>
        <el-collapse v-model="activeNames" class="runlog">
            <el-collapse-item title="运行日志" :name="status">
                <div>与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
                <div>在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。</div>
            </el-collapse-item>
        </el-collapse>
    </el-card>
</template>
<script>
    import sesectHosts from '../components/hosttransfer.vue'

    export default {
        components: {sesectHosts},

        data() {
            return {
                activeNames: ['open'],
                status: 'close',
                ruleForm: {
                    hosts: [],
                    cmd: '',
                },
                rules: {
                    cmd: [
                        {required: true, message: '请输入命令', trigger: 'blur'},
                    ]
                },
            };
        },

        created() {
        },
        methods: {
            postForm(formName) {
                this.status = 'open';
                console.log(formName)
            },
            getHosts(data) {
                this.ruleForm.hosts = data
            }
        }
    }
</script>

<style lang='scss'>
    .runcmd {
        width: 680px;
        margin-left: 40px;
    }

    .runlog {
        margin: 25px;
    }
</style>