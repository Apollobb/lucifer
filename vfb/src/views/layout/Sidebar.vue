<template>
    <el-menu mode="vertical" theme="dark" :default-active="$route.path" :unique-opened="true">
        <div class="logo">cmdb</div>
        <sidebar-item :routes='$router.options.routes'></sidebar-item>
    </el-menu>
</template>

<script>
    import SidebarItem from './SidebarItem';
    export default {
        components: {SidebarItem},
    }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
    .el-menu {
        min-height: 100%;
    }

    .logo {
        line-height: 50px;
        text-align: center;
        display: table-cell;
        vertical-align: middle;
        color: #1c8de0;
        padding-left: 60px;
    }
</style>
