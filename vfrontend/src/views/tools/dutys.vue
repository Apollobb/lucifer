<template>
    <div class="app-container calendar-list-container">
        <el-card class="filter-container">
            <el-input @keyup.enter.native="handleFilter" style="width: 110px;" class="filter-item" placeholder="值班人员"
                      v-model="listQuery.username__contains" icon="circle-close" :on-icon-click="handleIconClick">
            </el-input>
            <el-select clearable style="width: 90px" class="filter-item" v-model="listQuery.shift"
                       placeholder="班次">
                <el-option v-for="item in shiftOptions" :key="item" :label="item" :value="item">
                </el-option>
            </el-select>
            <el-date-picker
                    class="filter-item"
                    v-model="datefilter"
                    type="daterange"
                    placeholder="选择日期范围">
            </el-date-picker>
            <el-button class="filter-item" type="primary" v-waves icon="search" @click="handleFilter">搜索</el-button>
            <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="danger" icon="edit">
                添加交接记录


            </el-button>

            <el-table :data="tableData" v-loading.body="listLoading" border fit highlight-current-row style="width: 100%">
                <el-table-column prop='username' label='用户名' sortable>
                    <template scope="scope">
                        <el-popover trigger="hover" placement="top">
                            <p>性别: {{ scope.row.gender }}</p>
                            <p>性取向: {{ scope.row.orientation }}</p>
                            <div slot="reference" class="name-wrapper" style="text-align: center">
                                <el-tag>{{ scope.row.username }}</el-tag>
                            </div>
                        </el-popover>
                    </template>
                </el-table-column>
                <el-table-column prop='shift' label='班次' sortable></el-table-column>
                <el-table-column prop='time' label='交接时间' sortable></el-table-column>
                <el-table-column prop='content' label='交接内容'></el-table-column>
                <el-table-column prop='images' label='交接图片'>
                    <template scope="scope">
                        <el-popover trigger="hover" placement="top">
                            <img :src="scope.row.images">
                            <div slot="reference" class="name-wrapper" style="text-align: center">
                                <img :src="scope.row.images">
                            </div>
                        </el-popover>
                    </template>
                </el-table-column>
                <el-table-column prop='telephone' label='手机号'></el-table-column>
            </el-table>
            <div v-show="!listLoading" class="pagination-container">
                <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange"
                               :current-page.sync="currentPage"
                               :page-sizes="pagesize" :page-size="limit"
                               layout="total, sizes, prev, pager, next, jumper" :total="tabletotal">
                </el-pagination>
            </div>
        </el-card>

        <el-dialog title="添加交接记录" :visible.sync="dialogForm" size="large">
            <duty-add :shiftOptions="shiftOptions"></duty-add>
        </el-dialog>

    </div>
</template>

<script>
    import {getDutyList} from 'api/duty';
    import {LIMIT} from '@/config'
    import format from '@/utils/dateformat'
    import dutyAdd from './dutyadd.vue'

    export default {
        components: {
            dutyAdd
        },
        data() {
            return {
                tableData: [],
                tabletotal: 0,
                searchdata: '',
                currentPage: 1,
                limit: LIMIT,
                offset: '',
                pagesize: [10, 25, 50, 100],
                shiftOptions: ['早班', '中班', '晚班'],
                dialogForm: false,
                datefilter: '',
                searchQuery: {
                    username__contains: '',
                    shift: '',
                    time_lte: '',
                    time_gte: '',
                }
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
                    username__contains: this.searchdata
                };
                getDutyList(parms).then(response => {
                    this.tableData = response.data.results;
                    this.tabletotal = response.data.count;
                })
            },

            handleIconClick() {
                this.listQuery.username_like = ''
            },
            handleFilter() {
                this.listQuery.time_gte = format(new Date(this.datefilter[0]), 'YYYY-MM-DD');
                this.listQuery.time_lte = format(new Date(this.datefilter[1]), 'YYYY-MM-DD');
                this.getList();
            },
            handleSizeChange(val) {
                this.listQuery._limit = val;
                this.getList();
            },
            handleCurrentChange(val) {
                this.listQuery._page = val;
                this.getList();
            },
            handleCreate() {
                this.dialogForm = true;
            },
            formdata(data) {
                console.log(data);
                this.dialogForm = false;
            },
        }
    }
</script>

<style lang='scss'>
    .tips {
        color: #ff2ff7;
    }
</style>