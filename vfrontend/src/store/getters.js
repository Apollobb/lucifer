const getters = {
  sidebar: state => state.app.sidebar,
  visitedViews: state => state.app.visitedViews,
  token: state => state.user.token,
  islogin: state => state.user.islogin,
  token_time: state => state.user.token_time,
  userinfo: state => state.user.userinfo,
};
export default getters
