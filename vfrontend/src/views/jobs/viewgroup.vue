<template>
    <div>
        <el-card>
            <div class="head-lavel">
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
                    <el-table-column prop='name' label='项目名'></el-table-column>
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
    </div>
</template>

<script>
    import {getJobList} from 'api/job'
    import {LIMIT} from '@/config'

    export default {

        props: ['groupName'],
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
                rowdata: {}
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
                    group__name: this.groupName,
                    name__contains: this.searchdata
                };
                getJobList(parms).then(response => {
                    this.tableData = response.data.results;
                    this.tabletotal = response.data.count;
                })
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