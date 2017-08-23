const getters = {
  sidebar: state => state.app.sidebar,
  visitedViews: state => state.app.visitedViews,
  token: state => state.user.token,
  username: state => state.user.username,
  islogin: state => state.user.islogin,
  token_time: state => state.user.token_time,
  userinfo: state => state.user.userinfo,
};
export default getters
