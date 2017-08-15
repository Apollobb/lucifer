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
                    <el-table-column prop='hostname' label='主机名' sortable></el-table-column>
                    <el-table-column prop='ip' label='主机ip' sortable></el-table-column>
                    <el-table-column prop='status' label='状态' sortable>
                        <template scope="scope">
                            <div slot="reference" class="name-wrapper" style="text-align: center">
                                <el-tag :type="ASSET_STATUS[scope.row.status].type">
                                    {{ASSET_STATUS[scope.row.status].status}}
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
    import {getHostList} from 'api/asset';
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
                ASSET_STATUS: {
                    'used': {"status": "使用中", "type": "primary"},
                    'noused': {"status": "未使用", "type": "gray"},
                    'broken': {"status": "故障", "type": "danger"},
                    'other': {"status": "其他", "type": "warning"}
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
                    group__name: this.groupName,
                    name__contains: this.searchdata
                };
                getHostList(parms).then(response => {
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