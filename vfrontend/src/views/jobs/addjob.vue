<template xmlns="http://www.w3.org/1999/html">
    <el-form :model="rowdata" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="项目名称" prop="name">
            <el-input v-model="rowdata.name"></el-input>
        </el-form-item>
        <el-form-item label="项目类型" prop="jobs_type">
            <el-select v-model="rowdata.jobs_type" placeholder="请选择项目类型">
                <el-option v-for="item in jobs_type" :key="item.id" :value="item"></el-option>
            </el-select>
        </el-form-item>
        <div>
            <sesect-hosts :selecthost="rowdata.hosts" @gethosts="getHosts"></sesect-hosts>
        </div>
        <el-form-item label="项目分组" prop="group">
            <el-select v-model="rowdata.group" placeholder="请选择项目分组">
                <el-option v-for="item in groups" :key="item.name" :value="item.name"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="仓库类型" prop="code_repo">
            <el-select v-model="rowdata.code_repo" placeholder="请选择仓库类型">
                <el-option v-for="item in repo_type" :key="item.id" :value="item"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="代码地址" prop="code_url">
            <el-input v-model="rowdata.code_url"></el-input>
        </el-form-item>
        <el-form-item label="发布脚步" prop="deploy_script">
            <el-input type="textarea"
                      :autosize="{ minRows: 4, maxRows: 10}"
                      placeholder="请输入内容"
                      v-model="rowdata.deploy_script"></el-input>
        </el-form-item>
        <el-form-item label="项目描述" prop="desc">
            <el-input v-model="rowdata.desc"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="postForm('ruleForm')">提交</el-button>
            <el-button type="danger" @click="resetForm('ruleForm')">清空</el-button>
        </el-form-item>
    </el-form>
</template>
<script>
    import {postJob} from 'api/job';
    import {getJobGroupList} from 'api/job';
    import sesectHosts from '../components/hosttransfer.vue'

    export default {
        components: {sesectHosts},

        data() {
            return {
                rowdata: {
                    name: '',
                    jobs_type: '',
                    hosts: [],
                    group: '',
                    code_repo: '',
                    code_url: '',
                    deploy_script: '',
                    desc: ''
                },
                rules: {
                    name: [
                        {required: true, message: '请输入活动名称', trigger: 'blur'},
                    ],
                    jobs_type: [
                        {required: true, message: '请选择项目类型', trigger: 'blur'}
                    ],
                    group: [
                        {required: true, message: '请选择项目分组', trigger: 'change'},
                    ],
                    code_repo: [
                        {required: true, message: '请选择仓库类型', trigger: 'blur'}
                    ],
                    code_url: [
                        {required: true, message: '请输入代码地址', trigger: 'blur'},
                    ],
                    deploy_script: [
                        {required: true, message: '请填写发布脚步', trigger: 'blur'}
                    ]
                },
                jobs_type: ['php', 'python', 'java', 'nodejs'],
                repo_type: ['git', 'svn', 'ftp'],
                groups: '',
            };
        },

        created() {
            this.getGroups();
        },
        methods: {
            postForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        postJob(this.rowdata).then(response => {
                            if (response.statusText = 'ok') {
                                this.$message({
                                    type: 'success',
                                    message: '恭喜你，新建成功'
                                });
                            }
                        }).catch(error => {
                            this.$message.error('新建失败');
                            console.log(error);
                        });
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
                this.$emit('DialogStatus', false);
            },

            resetForm(formName) {
                this.rowdata.hosts = [];
                this.$refs[formName].resetFields();
            },
            getHosts(data) {
                this.rowdata.hosts = data
            },
            getGroups() {
                getJobGroupList().then(response => {
                    this.groups = response.data.results;
                })
            },
        }
    }
</script>

<style lang='scss'>

</style>