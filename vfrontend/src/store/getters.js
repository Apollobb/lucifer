const getters = {
  sidebar: state => state.app.sidebar,
  visitedViews: state => state.app.visitedViews,
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  name: state => state.user.name,
  username: state => state.user.username,
  email: state => state.user.email,
  islogin: state => state.user.islogin,
  roles: state => state.user.roles,
  token_time: state => state.user.token_time,
  userinfo: state => state.user.userinfo,
};
export default getters
