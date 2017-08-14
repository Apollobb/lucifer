<template>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-row :gutter="20">
            <el-col :span="12">
                <el-form-item label="班次" prop="shift">
                    <el-select v-model="ruleForm.shift" placeholder="请选择班次">
                        <el-option v-for="item in shiftOptions" :key="item" :label="item" :value="item"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="值班人员" prop="username">
                    <el-input v-model="ruleForm.username"></el-input>
                </el-form-item>
                <el-form-item label="值班内容" prop="content">
                    <mavon-editor default_open='edit' v-model="ruleForm.content" :toolbars="toolbars"/>
                </el-form-item>
            </el-col>
            <el-col :span="12">
                <el-upload
                        class="upload-demo"
                        ref="upload"
                        list-type="picture-card"
                        action="https://jsonplaceholder.typicode.com/posts/"
                        :on-success="handleSuccess"
                        :file-list="fileList"
                        :auto-upload="false">
                    <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
                    <div slot="tip" class="el-upload__tip">
                        <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器
                        </el-button>
                        <a>只能上传jpg/png文件，且不超过500kb</a>
                    </div>
                </el-upload>
            </el-col>
        </el-row>
        <el-form-item>
            <el-tooltip content="注意是否有上传图片到服务器" placement="top">
                <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
            </el-tooltip>
            <el-button type="warning" @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
    </el-form>
</template>
<script>
    import {postUpload, postDuty} from 'api/tool'

    export default {
        props: ['shiftOptions'],
        data() {
            return {
                fileList: [],
                ruleForm: {
                    username: '',
                    shift: '',
                    content: '',
                    images: [],
                },
                rules: {
                    username: [
                        {required: true, message: '请输入一个风骚的名字', trigger: 'blur'},
                    ],
                    shift: [
                        {required: true, message: '请选择班次', trigger: 'change'}
                    ]
                },
                toolbars: {
                    bold: true, // 粗体
                    italic: true, // 斜体
                    header: true, // 标题
                    underline: true, // 下划线
                    strikethrough: true, // 中划线
                    ol: true, // 有序列表
                    subfield: true, // 是否需要分栏
                    fullscreen: true, // 全屏编辑
                },
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs.upload.submit();
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        postDuty(this.ruleForm).then(response => {
                            if (response.statusText = 'ok') {
                                this.$message({
                                    type: 'success',
                                    message: '恭喜你，新建成功'
                                });
                                this.$emit('getedit', false);
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
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
                this.$refs.upload.clearFiles();
            },
            submitUpload() {
                this.$refs.upload.submit();
            },
            handleSuccess(file, fileList) {
                let formData = new FormData();
                formData.append('username', this.ruleForm.username);
                formData.append('file', fileList.raw);
                formData.append('type', fileList.raw.type.split("/")[0]);
                formData.append('archive', this.$route.name);
                postUpload(formData).then(response => {
                    this.ruleForm.images.push(response.data.file.filename);
                    if (response.statusText = 'ok') {
                        this.$message({
                            type: 'success',
                            message: '恭喜你，上传成功'
                        });
                    }
                }).catch(error => {
                    this.$message.error('上传失败');
                    this.$refs.upload.clearFiles();
                    console.log(error);
                });
            },
        }
    }
</script>

<style>

</style>