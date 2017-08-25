import {login, logout, getInfo} from 'api/auth';
import * as CookiesApi from 'utils/auth';

const user = {
    state: {
        code: '',
        token: CookiesApi.getToken(),
        islogin: false,
        userinfo: CookiesApi.getUserinfo(),
    },

    mutations: {
        SET_CODE: (state, code) => {
            state.code = code;
        },
        SET_TOKEN: (state, token) => {
            state.token = token;
        },
        SET_ISLOGIN: (state, islogin) => {
            state.islogin = islogin;
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
                CookiesApi.removeToken();
                CookiesApi.removeUserinfo();
                resolve();
            })
        },

        // 前端 登出
        FedLogOut({commit}) {
            return new Promise(resolve => {
                commit('SET_TOKEN', '');
                CookiesApi.removeToken();
                CookiesApi.removeUserinfo();
                resolve();
            })
        },

        // 获取用户信息
        getUserInfo({commit},username) {
            return new Promise((resolve, reject) => {
                getInfo(username).then(response => {
                    const data = response.data.results[0];
                    commit('SET_USERINFO', data);
                    CookiesApi.setUserinfo(data);
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
