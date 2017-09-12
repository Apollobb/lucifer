<template>
    <div class="app-wrapper" :class="{hideSidebar:!sidebar.opened}">
        <vue-particles class="particles"
                       color="#ffffff"
                       :particleOpacity="0.7"
                       :particlesNumber="80"
                       shapeType="circle"
                       :particleSize="4"
                       linesColor="#e71fff"
                       :linesWidth="2"
                       :lineLinked="true"
                       :lineOpacity="0.4"
                       :linesDistance="150"
                       :moveSpeed="3"
                       :hoverEffect="true"
                       hoverMode="grab"
                       :clickEffect="true"
                       clickMode="push"
        >
        </vue-particles>
        <div class="sidebar-wrapper">
            <Sidebar class="sidebar-container"/>
        </div>
        <div class="main-container">
            <Navbar/>
            <App-main/>
        </div>
    </div>
</template>

<script>
    import {Navbar, Sidebar, AppMain} from 'views/layout';

    export default {
        name: 'layout',
        components: {
            Navbar,
            Sidebar,
            AppMain
        },
        computed: {
            sidebar() {
                return this.$store.state.app.sidebar;
            }
        }
    }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
    @import "src/styles/mixin.scss";

    .particles {
        position: fixed;
        height: 100%;
        width: 100%;
        color: #ffffff;
        z-index: -1;
    }

    .app-wrapper {
        @include clearfix;
        position: relative;
        height: 100%;
        width: 100%;
        &.hideSidebar {
            .sidebar-wrapper {
                transform: translate(-140px, 0);
                .sidebar-container {
                    transform: translate(132px, 0);
                }
                &:hover {
                    transform: translate(0, 0);
                    .sidebar-container {
                        transform: translate(0, 0);
                    }
                }
            }
            .main-container {
                margin-left: 70px;
            }
        }
        .sidebar-wrapper {
            width: 200px;
            position: fixed;
            top: 0;
            bottom: 0;
            left: 0;
            z-index: 1001;
            overflow: hidden;
            transition: all .28s ease-out;
        }
        .sidebar-container {
            transition: all .28s ease-out;
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            overflow-y: scroll;
        }
        .main-container {
            min-height: 100%;
            transition: all .28s ease-out;
            margin-left: 200px;
        }
    }
</style>