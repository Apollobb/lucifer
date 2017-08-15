<template xmlns="http://www.w3.org/1999/html">
    <el-form :model="rowdata" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="主机名" prop="hostname">
            <el-input v-model="rowdata.hostname"></el-input>
        </el-form-item>
        <el-form-item label="主机ip" prop="ip">
            <el-input v-model="rowdata.ip"></el-input>
        </el-form-item>
        <el-form-item label="其他ip" prop="other_ip">
            <el-input v-model="rowdata.other_ip"></el-input>
        </el-form-item>
        <el-form-item label="分组" prop="group">
            <el-select v-model="rowdata.group" multiple placeholder="请选择分组">
                <el-option v-for="item in groups" :key="item.name" :value="item.name"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="设备类型" prop="asset_type">
            <el-select v-model="rowdata.asset_type" placeholder="请选择设备类型">
                <el-option v-for="item in ASSET_TYPE" :key="item.id" :value="item.key">{{item.name}}</el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="主机状态" prop="status">
            <el-select v-model="rowdata.status" placeholder="请选择主机状态">
                <el-option v-for="item in ASSET_STATUS" :key="item.id" :value="item.key">{{item.name}}</el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="系统" prop="os">
            <el-input v-model="rowdata.os"></el-input>
        </el-form-item>
        <el-form-item label="cpu型号" prop="cpu_model">
            <el-input v-model="rowdata.cpu_model"></el-input>
        </el-form-item>
        <el-form-item label="cpu个数" prop="cpu_num">
            <el-input v-model="rowdata.cpu_num"></el-input>
        </el-form-item>
        <el-form-item label="内存" prop="memory">
            <el-input v-model="rowdata.memory"></el-input>
        </el-form-item>
        <el-form-item label="磁盘" prop="disk">
            <el-input v-model="rowdata.disk"></el-input>
        </el-form-item>
        <el-form-item label="备注" prop="memo">
            <el-input v-model="rowdata.memo"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="putForm('ruleForm')">提交</el-button>
        </el-form-item>
    </el-form>
</template>
<script>
    import {putHost, getHostGroupList} from 'api/asset';

    export default {
        components: {},

        props: ['rowdata'],
        data() {
            return {
                rules: {
                    hostname: [
                        {required: true, message: '请输入主机名', trigger: 'blur'},
                    ],
                    ip: [
                        {required: true, message: '请输入主机ip', trigger: 'blur'}
                    ],
                    other_ip: [
                        {required: true, message: '请输入主机其他ip', trigger: 'blur'}
                    ],
                    group: [
                        {required: true, type: 'array', message: '请选择项目分组', trigger: 'change'},
                    ],
                    asset_type: [
                        {required: true, message: '请选择设备类型', trigger: 'change'}
                    ],
                    status: [
                        {required: true, message: '请输入主机状态', trigger: 'blur'},
                    ],
                },
                ASSET_STATUS: [
                    {key: 'used', name: "使用中"},
                    {key: 'noused', name: "未使用"},
                    {key: 'broken', name: "故障"},
                    {key: 'other', name: "其它"},
                ],
                ASSET_TYPE: [
                    {key: 'physical', name: "物理机"},
                    {key: 'virtual', name: "虚拟机"},
                    {key: 'container', name: "容器"},
                    {key: 'network', name: "网络设备"},
                    {key: 'other', name: "其他设备"},
                ],
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
                        putHost(this.rowdata.id, this.rowdata).then(response => {
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

            resetForm(formName) {
                this.rowdata.hosts = [];
                this.$refs[formName].resetFields();
            },
            getGroups() {
                getHostGroupList().then(response => {
                    this.groups = response.data.results;
                })
            },
        }
    }
</script>

<style lang='scss'>

</style>