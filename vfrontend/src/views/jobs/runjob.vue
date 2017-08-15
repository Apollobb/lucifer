<template xmlns="http://www.w3.org/1999/html">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="发布环境" prop="deploy_env">
            <el-select v-model="ruleForm.deploy_env" placeholder="请选择发布环境">
                <el-option v-for="item in deploy_env" :key="item.id" :value="item"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="选择发布机器" prop="hosts">
            <el-select v-model="ruleForm.hosts" multiple placeholder="请选择发布机器">
                <el-option v-for="item in hosts" :key="item.id" :value="item"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="代码分支" prop="code_branch">
            <el-select v-model="ruleForm.code_branch" placeholder="请选择代码分支">
                <el-option v-for="item in code_branch" :key="item.id" :value="item"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="runForm('ruleForm')">提交</el-button>
        </el-form-item>
    </el-form>
</template>
<script>
    export default {
        components: {},

        props: ['hosts', 'deploy_env', 'code_branch'],
        data() {
            return {
                ruleForm: {
                    deploy_env: '',
                    hosts: [],
                    code_branch: ''
                },
                rules: {
                    deploy_env: [
                        {required: true, message: '请选择发布环境', trigger: 'change'}
                    ],
                    hosts: [
                        {required: true, type: 'array', message: '请选择发布主机', trigger: 'change'}
                    ],
                    code_branch: [
                        {required: true, message: '请选择代码分支', trigger: 'change'}
                    ],
                },
            };
        },

        created() {
        },
        methods: {
            runForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        console.log(this.ruleForm);
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
                this.$emit('DialogStatus', false);
            }
        }
    }
</script>

<style lang='scss'>

</style>