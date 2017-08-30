<template>
    <div>
        <el-menu class="navbar" mode="horizontal">
            <hamburger class="hamburger-container" :toggleClick="toggleSideBar" :isActive="sidebar.opened"></hamburger>

            <tabs-view></tabs-view>
            <screenfull class='screenfull'></screenfull>
            <el-dropdown class="avatar-container" trigger="hover">
                <div class="avatar-wrapper">
                    <img class="user-avatar" :src="'upload' + UserInfo.avatar+'?imageView2/1/w/80/h/80'">
                    <i class="el-icon-caret-bottom"></i>
                </div>
                <el-dropdown-menu class="user-dropdown" slot="dropdown">
                    <el-dropdown-item @click.native="changeava=true">
                        修改头像
                    </el-dropdown-item>
                    <el-dropdown-item @click.native="changepw=true">
                        修改密码
                    </el-dropdown-item>
                    <el-dropdown-item divided><span @click="logout" style="display:block;">退出登录</span>
                    </el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </el-menu>

        <el-dialog title="修改密码" :visible.sync="changepw" size="tiny">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                <el-form-item label="密码" prop="new_password1">
                    <el-input type="password" v-model="ruleForm.new_password1"></el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="new_password2">
                    <el-input type="password" v-model="ruleForm.new_password2"></el-input>
                </el-form-item>
                <el-form-item class="btn">
                    <el-button type="primary" @click="ChangePasswd('ruleForm')">提交</el-button>
                    <el-button type="danger" @click="resetForm('ruleForm')">清空</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>

        <el-dialog title="修改头像" :visible.sync="changeava" size="tiny">
            <avatar-upload :userinfo="UserInfo"></avatar-upload>
        </el-dialog>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import Levelbar from './Levelbar';
    import TabsView from './TabsView';
    import Hamburger from 'components/Hamburger';
    import Screenfull from 'components/Screenfull';
    import avatarUpload from '../components/avatarUpload';
    import {changePassword} from 'api/auth'

    export default {
        components: {
            Levelbar,
            TabsView,
            Hamburger,
            Screenfull,
            avatarUpload,
        },
        data() {
            const validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入新密码'));
                } else if (!/(?=.*\d)(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9])/.test(value)) {
                    callback(new Error('密码中必须包含字母、数字、特称字符'));
                } else {
                    if (this.ruleForm.new_password2 !== '') {
                        // 对第二个密码框单独验证
                        this.$refs.ruleForm.validateField('new_password2');
                    }
                    callback();
                }
            };
            const validatePassCheck = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.ruleForm.new_password1) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return {
                UserInfo: '',
                ruleForm: {
                    new_password1: '',
                    new_password2: ''
                },
                rules: {
                    new_password1: [
                        {required: true, trigger: 'blur', validator: validatePass},
                        {min: 8, max: 16, message: '长度在 8 到 16 个字符', trigger: 'blur'}
                    ],
                    new_password2: [
                        {required: true, trigger: 'blur', validator: validatePassCheck},
                        {min: 8, max: 16, message: '长度在 8 到 16 个字符', trigger: 'blur'}
                    ],
                },
                changepw: false,
                changeava: false,
            }
        },
        computed: {
            ...mapGetters([
                'sidebar',
                'userinfo',
            ]),
        },
        created() {
            this.getUserinfo();
        },

        methods: {
            getUserinfo() {
                this.UserInfo = JSON.parse(this.userinfo)
            },
            toggleSideBar() {
                this.$store.dispatch('ToggleSideBar')
            },
            logout() {
                this.$store.dispatch('LogOut').then(() => {
                    location.reload();// 为了重新实例化vue-router对象 避免bug
                });
            },
            ChangePasswd(formName) {
                this.changepw = true;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        changePassword(this.ruleForm).then(response => {
                            if (response.statusText = 'ok') {
                                this.changepw = false;
                                this.$message({
                                    type: 'success',
                                    message: '恭喜你，密码更改成功'
                                });
                            }
                        }).catch(error => {
                            this.$message.error('更改失败');
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
            },
        }
    }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
    .navbar {
        height: 50px;
        line-height: 50px;
        border-radius: 0px !important;
        /*position:fixed;*/
        /*top:0;*/
        /*z-index: 999;*/
        .hamburger-container {
            line-height: 58px;
            height: 50px;
            float: left;
            padding: 0 10px;
        }
        .screenfull {
            position: absolute;
            right: 90px;
            top: 16px;
            color: red;
        }
        .avatar-container {
            height: 50px;
            display: inline-block;
            position: absolute;
            right: 35px;
            .avatar-wrapper {
                cursor: pointer;
                margin-top: 5px;
                position: relative;
                .user-avatar {
                    width: 40px;
                    height: 40px;
                    border-radius: 10px;
                }
                .el-icon-caret-bottom {
                    position: absolute;
                    right: -20px;
                    top: 25px;
                    font-size: 12px;
                }
            }
        }

        .btnAvatar {
        }
    }
</style>



