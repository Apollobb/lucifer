<template>
    <div>
        <el-card>
            <div class="head-lavel">
                <div class="table-button">
                    <el-button type="info" icon="plus" @click="handleCreate">新建项目</el-button>
                </div>
                <div class="table-search">
                    <el-input
                            placeholder="搜索 ..."
                            icon="search"
                            v-model="searchdata"
                            @keyup.enter.native="searchClick"
                            :on-icon-click="searchClick">
                    </el-input>
                </div>
            </div>
            <div>
                <el-table :data="tableData" border style="width: 100%">
                    <el-table-column prop='name' label='项目名' sortable>
                        <template scope="scope">
                            <div slot="reference" class="name-wrapper" style="text-align: center">
                                <el-button type="text" @click="handleEdit(scope.row)">{{ scope.row.name }}</el-button>
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column prop='hosts' label='被发布的主机'>
                        <template scope="scope">
                            <el-popover trigger="hover" placement="top">
                                <p v-for="item in scope.row.hosts" :key="item.id">{{ item }}</p>
                                <div slot="reference" class="name-wrapper" style="text-align: center">
                                    <el-tag color="green">{{ scope.row.hosts[0] }}</el-tag>
                                </div>
                            </el-popover>
                        </template>
                    </el-table-column>
                    <el-table-column prop='group' label='所在组' sortable></el-table-column>
                    <el-table-column prop='deploy_status' label='发布状态' sortable='custom'
                                     :filters="[{ text: '未执行', value: 'unexecuted' }, { text: '发布中', value: 'deploy' }, { text: '发布成功', value: 'succed' }, { text: '发布失败', value: 'failed' }]"
                                     :filter-method="filterTag"
                                     filter-placement="bottom-end">
                        <template scope="scope">
                            <div slot="reference" class="name-wrapper" style="text-align: center">
                                <el-tag :type="DEPLOY_STATUS[scope.row.deploy_status].type">
                                    {{DEPLOY_STATUS[scope.row.deploy_status].status}}

                                </el-tag>
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column prop='update_time' label='发布时间' sortable></el-table-column>
                    <el-table-column prop='cost_time' label='发布所用时间' sortable></el-table-column>
                    <el-table-column label="操作">
                        <template scope="scope">
                            <el-button @click="handleRun(scope.row)" type="success" size="small">执行</el-button>
                            <el-button type="info" size="small" disabled>查看</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
            <div class="table-pagination">
                <el-pagination
                        small
                        @size-change="handleSizeChange"
                        @current-change="handleCurrentChange"
                        :current-page.sync="currentPage"
                        :page-sizes="pagesize"
                        :page-size="limit"
                        layout="prev, pager, next, sizes"
                        :total="tabletotal">
                </el-pagination>
            </div>
        </el-card>
        <el-dialog :title="textMap[dialogStatus]" :visible.sync="addForm" size="small">
            <add-project @DialogStatus="getDialogStatus"></add-project>
        </el-dialog>
        <el-dialog :title="textMap[dialogStatus]" :visible.sync="editForm" size="small">
            <edit-project :rowdata="rowdata" @DialogStatus="getDialogStatus"></edit-project>
        </el-dialog>
        <el-dialog :title="textMap[dialogStatus]" :visible.sync="runForm" size="tiny">
            <run-project :hosts="rowdata.hosts" :deploy_env="deploy_env" :code_branch="code_branch" @DialogStatus="getDialogStatus"></run-project>
        </el-dialog>
    </div>
</template>

<script>
    import {getJobList} from 'api/job'
    import {LIMIT} from '@/config'
    import addProject from './addjob.vue'
    import editProject from './editjob.vue'
    import runProject from './runjob.vue'
    import {getHostList} from 'api/asset'

    export default {
        components: {addProject, editProject, runProject},
        data() {
            return {
                tableData: [],
                tabletotal: 0,
                searchdata: '',
                currentPage: 1,
                limit: LIMIT,
                offset: '',
                pagesize: [10, 25, 50, 100],
                DEPLOY_STATUS: {
                    'unexecuted': {"status": "未执行", "type": "gray"},
                    'deploy': {"status": "发布中", "type": "primary"},
                    'succed': {"status": "发布成功", "type": "success"},
                    'failed': {"status": "发布失败", "type": "danger"}
                },
                addForm: false,
                editForm: false,
                runForm: false,
                rowdata: {},
                dialogStatus: '',
                textMap: {
                    create: '新建',
                    edit: '编辑',
                    run: '构建'
                },
                deploy_env: ['test','stagging','pre','prod'],
                code_branch: ['master','dev','test'],
            }
        },

        created() {
            this.fetchData();
        },
        methods: {
            fetchData() {
                const parms = {
                    limit: this.limit,
                    offset: this.offset,
                    name__contains: this.searchdata
                };
                getJobList(parms).then(response => {
                    this.tableData = response.data.results;
                    this.tabletotal = response.data.count;
                })
            },

            getDialogStatus(data) {
                this.editForm = data;
                this.addForm = data;
                this.runForm = data;
                this.fetchData();
            },

            handleCreate() {
                this.reseRowdata();
                this.dialogStatus = 'create';
                this.addForm = true;
            },

            handleEdit(row) {
                this.rowdata = Object.assign({}, row);
                this.dialogStatus = 'edit';
                this.editForm = true;
            },

            handleRun(row) {
                this.rowdata = Object.assign({}, row);
                this.dialogStatus = 'run';
                this.runForm = true;
            },
            reseRowdata() {
                this.rowdata = {
                    name: '',
                    deploy_env: '',
                    jobs_type: '',
                    hosts: [],
                    group: '',
                    code_repo: '',
                    code_url: '',
                    code_branch: '',
                    deploy_script: '',
                    desc: ''
                }
            },
            searchClick() {
                this.fetchData();
            },
            handleSizeChange(val) {
                this.limit = val;
                this.fetchData();
            },
            handleCurrentChange(val) {
                this.offset = val - 1;
                this.fetchData();
            },
            filterTag(value, row) {
                return row.deploy_status === value;
            },
        },
    }
</script>

<style lang='scss'>
    .head-lavel {
        padding-bottom: 50px;
    }

    .table-button {
        float: left;
    }

    .table-search {
        float: right;
    }

    .table-pagination {
        padding: 10px 0;
        float: right;
    }
</style>