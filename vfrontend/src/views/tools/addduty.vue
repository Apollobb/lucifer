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
                        action="https://jsonplaceholder.typicode.com/posts/"
                        :on-error="handleError"
                        :on-success="handleSuccess"
                        list-type="picture-card"
                        ref="upload">
                    <el-button size="small" type="primary">上传图片</el-button>
                    <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb, <span style="color: red">if not, you will be destory!</span>
                    </div>
                </el-upload>
            </el-col>
        </el-row>
        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
    </el-form>
</template>
<script>
    export default {
        props: ['shiftOptions'],
        data() {
            return {
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
                        this.$message({
                            message: '恭喜你，添加成功',
                            type: 'success'
                        });
                        this.$emit('formdata', this.ruleForm)
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
            handleError(err, file, fileList) {
                this.$message({
                    message: file.name + '图片不符合要求，上传失败！',
                    type: 'error'
                });
            },
            handleSuccess(response, file, fileList) {
                this.ruleForm.images.push(file.url)
            }
        }
    }
</script>