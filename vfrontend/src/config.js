/**
 * Created by Itimor on 2017/7/12.
 */

let CONFIG;
// if (process.env.NODE_ENV === 'development') {
if (process.env.NODE_ENV === 'production') {
    CONFIG = {
        apiUrl: "",
    };
} else {
    CONFIG = {
        apiUrl: "http://localhost:8000",
    };
}

//接口API根地址
const url = CONFIG.apiUrl;

module.exports = {
    apiUrl: url,

    //数据分页限制
    LIMIT: 10,

    //qiniu 上传到七牛
    qn_ack: 'Q0IABHxpUZfWiUxzWdT6cMXQKusAmTsfX_fiCWC2',
    qn_sek: 'qQ6Rjq3Kz8k05xEI9GG1T74BHg-EThAfgwJbaw8S',

    //本地上传到服务器
    uploads: `${url}/api/upload/`,

    //登录
    //login: `${url}/api-token-auth/`,
    login: `${url}/api-token-auth/`,
    changePassword: `${url}/api/changepasswd/`,

    //主机
    hosts: `${url}/api/hosts/`,
    hostgroups: `${url}/api/hostgroups/`,

    //用户
    users: `${url}/api/users/`,
    groups: `${url}/api/groups/`,
    roles: `${url}/api/roles/`,

    //值班
    dutys: `${url}/api/dutys/`,

    //发布项目
    jobs: `${url}/api/jobs/`,
    jobgroups: `${url}/api/jobgroups/`,
};