import {login, logout, getInfo} from 'api/auth';
import * as CookiesApi from 'utils/auth';

const user = {
    state: {
        code: '',
        token: CookiesApi.getToken(),
        uid: '',
        username: '',
        email: '',
        islogin: false,
        name: CookiesApi.getName(),
        token_time: CookiesApi.getTokenTime(),
        avatar: CookiesApi.getAvatar(),
        roles: CookiesApi.getRoles(),
        userinfo: ''
    },

    mutations: {
        SET_CODE: (state, code) => {
            state.code = code;
        },
        SET_UID: (state, uid) => {
            state.uid = uid;
        },
        SET_TOKEN: (state, token) => {
            state.token = token;
        },
        SET_USERNAME: (state, username) => {
            state.username = username;
        },
        SET_EMAIL: (state, email) => {
            state.email = email;
        },
        SET_ISLOGIN: (state, islogin) => {
            state.islogin = islogin;
        },
        SET_NAME: (state, name) => {
            state.name = name;
        },
        SET_AVATAR: (state, avatar) => {
            state.avatar = avatar;
        },
        SET_ROLES: (state, roles) => {
            state.roles = roles;
        },
        SET_USERINFO: (state, userinfo) => {
            state.userinfo = userinfo;
        },
        SET_TOKEN_TIME: (state, token_time) => {
            state.token_time = token_time;
        },
        LOGIN_SUCCESS: () => {
            console.log('login success')
        },
        LOGOUT_USER: state => {
            state.user = '';
        }
    },

    actions: {
        Login({commit}, userInfo) {
            return new Promise((resolve, reject) => {
                login(userInfo).then(response => {
                    const cur_date = new Date().getTime();
                    CookiesApi.setToken(response.data.token);
                    CookiesApi.setTokenTime(cur_date);
                    commit('SET_TOKEN', response.data.token);
                    commit('SET_USERNAME', userInfo.username);
                    commit('SET_ISLOGIN', true);
                    commit('SET_TOKEN_TIME', cur_date);
                    resolve();
                }).catch(error => {
                    reject(error)
                })
            })
        },

        // 登出
        LogOut({commit, state}) {
            return new Promise((resolve, reject) => {
                commit('SET_TOKEN', ''),
                commit('SET_ROLES', []);
                CookiesApi.removeToken();
                CookiesApi.removeTokenTime();
                CookiesApi.removeName();
                CookiesApi.removeAvatar();
                CookiesApi.removeRoles();
                resolve();
            })
        },

        // 前端 登出
        FedLogOut({commit}) {
            return new Promise(resolve => {
                commit('SET_TOKEN', '');
                CookiesApi.removeToken();
                resolve();
            })
        },

        // 获取用户信息
        GetInfo({commit, state}) {
            return new Promise((resolve, reject) => {
                getInfo(state.username).then(response => {
                    const data = response.data.results[0];
                    commit('SET_USERINFO', data);
                    CookiesApi.setAvatar(data.avatar);
                    CookiesApi.setName(data.name);
                    CookiesApi.setRoles(data.roles);
                    console.log(CookiesApi.getAvatar());
                    resolve(response);
                }).catch(error => {
                    reject(error);
                })
            })
        },

        // 动态修改权限
        ChangeRole({commit}, role) {
            return new Promise(resolve => {
                commit('SET_ROLES', [role])
                resolve();
            })
        }
    }
};

export default user;
