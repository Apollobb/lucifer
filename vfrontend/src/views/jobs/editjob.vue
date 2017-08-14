<template xmlns="http://www.w3.org/1999/html">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="项目名称" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>
        <el-form-item label="发布环境" prop="deploy_env">
            <el-select v-model="ruleForm.deploy_env" multiple placeholder="请选择发布环境">
                <el-option v-for="item in ruleForm.deploy_env" :key="item.id" :value="item"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="项目类型" prop="jobs_type">
            <el-input v-model="ruleForm.jobs_type"></el-input>
        </el-form-item>
        <div>
            <sesect-hosts :selecthost="rowdata.hosts" @gethosts="getHosts"></sesect-hosts>
        </div>
        <el-form-item label="项目分组" prop="group">
            <el-select v-model="ruleForm.group" placeholder="请选择项目分组">
                <el-option v-for="item in groups" :key="item.name" :value="item.name"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="仓库类型" prop="code_repo">
            <el-input v-model="ruleForm.code_repo"></el-input>
        </el-form-item>
        <el-form-item label="代码地址" prop="code_url">
            <el-input v-model="ruleForm.code_url"></el-input>
        </el-form-item>
        <el-form-item label="代码分支" prop="code_branch">
            <el-select v-model="ruleForm.code_branch" multiple placeholder="请选择代码分支">
                <el-option v-for="item in ruleForm.code_branch" :key="item.id" :value="item"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="发布脚步" prop="deploy_script">
            <el-input type="textarea"
                      :autosize="{ minRows: 4, maxRows: 10}"
                      placeholder="请输入内容"
                      v-model="ruleForm.deploy_script"></el-input>
        </el-form-item>
        <el-form-item label="项目描述" prop="desc">
            <el-input v-model="ruleForm.desc"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="putForm('ruleForm')">提交</el-button>
            <el-button type="danger" @click="deleteForm">删除</el-button>
        </el-form-item>
    </el-form>
</template>
<script>
    import {deleteJob, putJob, getJobGroupList} from 'api/job';
    import sesectHosts from '../components/hosttransfer.vue'

    export default {
        components: {sesectHosts},

        props: ['rowdata'],
        data() {
            return {
                ruleForm: {
                    name: this.rowdata.name,
                    deploy_env: this.rowdata.deploy_env.split(","),
                    jobs_type: this.rowdata.jobs_type,
                    hosts: this.rowdata.hosts,
                    group: this.rowdata.group,
                    code_repo: this.rowdata.code_repo,
                    code_url: this.rowdata.code_url,
                    code_branch: this.rowdata.code_branch.split(","),
                    deploy_script: this.rowdata.deploy_script,
                    desc: this.rowdata.desc
                },
                rules: {
                    name: [
                        {required: true, message: '请输入活动名称', trigger: 'blur'},
                    ],
                    deploy_env: [
                        {required: true, type: 'array', message: '请选择发布环境', trigger: 'blur'}
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
                    code_branch: [
                        {required: true, type: 'array', message: '请选择代码分支', trigger: 'blur'}
                    ],
                    deploy_script: [
                        {required: true, message: '请填写发布脚步', trigger: 'blur'}
                    ]
                },
                groups: '',
            };
        },

        created() {
            this.getGroups();
        },
        methods: {
            putForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.ruleForm.code_branch = this.ruleForm.code_branch.toString();
                        this.ruleForm.deploy_env = this.ruleForm.deploy_env.toString();
                        putJob(this.rowdata.id, this.ruleForm).then(response => {
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
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
                this.$emit('getedit', false);
            },
            deleteForm(id) {
                this.$alert('骚年，你确定要这么干！！', '删除', {
                    confirmButtonText: '确定',
                    callback: action => {
                        this.$message({
                            type: 'info',
                            message: `action: ${ id }`
                        });
                    }
                });
            },
            getHosts(data) {
                this.ruleForm.hosts = data
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