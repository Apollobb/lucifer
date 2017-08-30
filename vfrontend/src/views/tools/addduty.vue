<template>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-row :gutter="20">
            <el-col :span="12">
                <el-form-item label="班次" prop="shift">
                    <el-select v-model="ruleForm.shift" placeholder="请选择班次">
                        <el-option v-for="item in shiftOptions" :key="item.value" :label="item.key" :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="值班人员" prop="username">
                    <el-input v-model="ruleForm.username"></el-input>
                </el-form-item>
                <el-form-item label="值班内容" prop="content">
                    <mavon-editor default_open='edit' v-model="ruleForm.content" :toolbars="toolbars"/>
                </el-form-item>
                <el-form-item label="上传图片" prop="content">
                    <el-switch
                            v-model="showUpload"
                            on-color="#13ce66"
                            off-color="#ff4949">
                    </el-switch>
                </el-form-item>
            </el-col>
            <el-col :span="12">
                <el-upload
                        v-show="ruleForm.username&&showUpload?true:false"
                        class="upload-demo"
                        ref="upload"
                        list-type="picture-card"
                        action="https://jsonplaceholder.typicode.com/posts/"
                        :on-success="handleSuccess"
                        :file-list="fileList"
                        :disabled="count>1?true:false">
                    <el-button slot="trigger" size="small" type="primary" :disabled="count>1?true:false">选择图片

                    </el-button>
                    <div slot="tip" class="el-upload__tip">
                        <p>只能上传jpg/png文件，且不超过500kb，<a style="color: red">最多只能上传两张图片</a></p>
                    </div>
                </el-upload>
            </el-col>
        </el-row>
        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
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
                count: 0,
                showUpload: false,
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
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        postDuty(this.ruleForm).then(response => {
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
                        this.$emit('DialogStatus', false);
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
                this.$refs.upload.clearFiles();
                this.count = 0
            },
            submitUpload() {
                this.$refs.upload.submit();
            },
            handleSuccess(file, fileList) {
                let formData = new FormData();
                formData.append('username', this.ruleForm.username);
                formData.append('file', fileList.raw);
                formData.append('pid', fileList.raw.uid);
                formData.append('type', fileList.raw.type);
                formData.append('archive', this.$route.path);
                postUpload(formData).then(response => {
                    console.log(fileList.raw);
                    this.ruleForm.images.push(response.data.filepath);
                    if (response.statusText = 'ok') {
                        this.count += 1;
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