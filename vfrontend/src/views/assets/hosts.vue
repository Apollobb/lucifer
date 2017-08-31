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
                    <el-table-column prop='hostname' label='主机名' sortable>
                        <template scope="scope">
                            <div slot="reference" class="name-wrapper" style="text-align: center">
                                <el-button type="text" @click="handleEdit(scope.row)">{{ scope.row.hostname }}
                                </el-button>
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column prop='ip' label='主机ip' sortable>
                        <template scope="scope">
                            <el-popover trigger="hover" placement="top">
                                <p>其他ip: {{ scope.row.other_ip }}</p>
                                <div slot="reference" class="name-wrapper" style="text-align: center">
                                    <el-tag>{{ scope.row.ip }}</el-tag>
                                </div>
                            </el-popover>
                        </template>
                    </el-table-column>
                    <el-table-column prop='group' label='所在组' sortable>
                        <template scope="scope">
                            <div v-for="item in scope.row.group" :key="item.id" slot="reference" class="name-wrapper"
                                 style="text-align: center">
                                <el-tag type="warning">{{item}}</el-tag>
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column prop='asset_type' label='类型' sortable>
                        <template scope="scope">
                            <div slot="reference" class="name-wrapper" style="text-align: center">
                                <el-tag :color="ASSET_TYPE[scope.row.asset_type].color">
                                    {{ASSET_TYPE[scope.row.asset_type].type}}

                                </el-tag>
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column prop='status' label='状态' sortable>
                        <template scope="scope">
                            <div slot="reference" class="name-wrapper" style="text-align: center">
                                <el-tag :type="ASSET_STATUS[scope.row.status].type">
                                    {{ASSET_STATUS[scope.row.status].status}}
                                </el-tag>
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column prop='os' label='系统'></el-table-column>
                    <el-table-column prop='cpu_model' label='cpu型号'></el-table-column>
                    <el-table-column prop='cpu_num' label='cpu个数' sortable></el-table-column>
                    <el-table-column prop='memory' label='内存(M)' sortable></el-table-column>
                    <el-table-column prop='disk' label='磁盘(G)' sortable></el-table-column>
                    <el-table-column prop='memo' label='备注'></el-table-column>
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
            <add-host @DialogStatus="getDialogStatus"></add-host>
        </el-dialog>
        <el-dialog :title="textMap[dialogStatus]" :visible.sync="editForm" size="small">
            <edit-host :rowdata="rowdata" @DialogStatus="getDialogStatus"></edit-host>
        </el-dialog>
    </div>
</template>

<script>
    import {getHostList} from 'api/asset';
    import {LIMIT} from '@/config'
    import addHost from './addhost.vue'
    import editHost from './edithost.vue'

    export default {
        components: {addHost, editHost},
        data() {
            return {
                tableData: [],
                tabletotal: 0,
                searchdata: '',
                currentPage: 1,
                limit: LIMIT,
                offset: '',
                pagesize: [10, 25, 50, 100],
                ASSET_TYPE: {
                    'physical': {"type": "物理机", "color": "#37474F"},
                    'virtual': {"type": "虚拟机", "color": "#7986cb"},
                    'container': {"type": "容器", "color": "#f06292"},
                    'network': {"type": "网络设备", "color": "#4dd0e1"},
                    'other': {"type": "其他设备", "color": "#d4e157"},
                },
                ASSET_STATUS: {
                    'used': {"status": "使用中", "type": "primary"},
                    'noused': {"status": "未使用", "type": "gray"},
                    'broken': {"status": "故障", "type": "danger"},
                    'other': {"status": "其他", "type": "warning"}
                },
                addForm: false,
                editForm: false,
                rowdata: {},
                dialogStatus: '',
                textMap: {
                    create: '新建',
                    edit: '编辑',
                    run: '构建'
                },
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
                getHostList(parms).then(response => {
                    this.tableData = response.data.results;
                    this.tabletotal = response.data.count;
                })
            },

            getDialogStatus(data) {
                this.editForm = data;
                this.addForm = data;
                this.fetchData();
            },

            handleCreate() {
                this.reseRowdata();
                this.dialogStatus = 'create';
                this.addForm = true;
            },
            handleEdit(row) {
                this.editForm = true;
                this.rowdata = row
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
            reseRowdata() {
                this.rowdata = {
                    hostname: '',
                    ip: '',
                    other_ip: '',
                    group: '',
                    asset_type: '',
                    status: '',
                    os: '',
                    cpu_model: '',
                    cpu_num: '',
                    memory: '',
                    disk: '',
                    memo: ''
                }
            }
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