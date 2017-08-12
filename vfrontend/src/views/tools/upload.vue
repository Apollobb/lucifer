<template>
    <div>
        <el-card>
            <div class="head-lavel">
                <div class="table-button">
                    <el-button type="info" icon="plus" @click="addForm=true"></el-button>
                </div>
                <div class="table-search">
                    <el-input @keyup.enter.native="handleFilter" style="width: 110px;" class="filter-item"
                              placeholder="上传人员"
                              v-model="listQuery.username__contains" icon="circle-close"
                              :on-icon-click="handleIconClick">
                    </el-input>
                    <el-input @keyup.enter.native="handleFilter" style="width: 110px;" class="filter-item"
                              placeholder="文件类型"
                              v-model="listQuery.type" icon="circle-close"
                              :on-icon-click="handleIconClick">
                    </el-input>
                    <el-date-picker
                            class="filter-item"
                            v-model="datefilter"
                            type="daterange"
                            placeholder="选择日期范围">
                    </el-date-picker>
                    <el-button class="filter-item" type="primary" icon="search" @click="searchClick">搜索
                    </el-button>
                </div>
            </div>
            <div>
                <el-table :data="tableData" @select="handleSelect" order style="width: 100%">
                    <el-table-column type="selection"></el-table-column>
                    <el-table-column prop='username' label='用户名' sortable></el-table-column>
                    <el-table-column prop='type' label='文件类型' sortable></el-table-column>
                    <el-table-column prop='size' label='文件大小'></el-table-column>
                    <el-table-column prop='file' label='文件地址' sortable></el-table-column>
                    <el-table-column prop='date' label='创建时间' sortable></el-table-column>
                </el-table>
            </div>
            <div class="table-footer">
                <div class="table-button">
                    <el-button type="danger" icon="delete" :disabled="butstatus" @click="deleteForm">删除记录</el-button>
                </div>
                <div class="table-pagination">
                    <el-pagination
                            small
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange"
                            :current-page.sync="listQuery.offset"
                            :page-sizes="pagesize"
                            :page-size="listQuery.limit"
                            layout="prev, pager, next, sizes"
                            :total="tabletotal">
                    </el-pagination>
                </div>
            </div>
        </el-card>
    </div>
</template>

<script>
    import {getUploadList, deleteUpload} from 'api/tool'
    import {LIMIT} from '@/config'
    import format from '@/utils/dateformat'

    export default {
        components: {},
        data() {
            return {
                tableData: [],
                tabletotal: 0,
                searchdata: '',
                pagesize: [10, 25, 50, 100],
                rowdata: {},
                selectId: [],
                butstatus: true,
                listQuery: {
                    offset: 0,
                    limit: LIMIT,
                    username__contains: '',
                    type: '',
                    date_lte: '',
                    date_gte: '',
                },
                datefilter: [],
            }
        },

        created() {
            this.fetchData();
        },

        methods: {
            fetchData() {
                getUploadList(this.listQuery).then(response => {
                    this.tableData = response.data.results;
                    this.tabletotal = response.data.count;
                })
            },

            getEdit(data) {
                setTimeout(this.fetchData, 3000);
                this.addForm = data;
            },
            handleIconClick() {
                this.listQuery.username__contains = ''
            },
            searchClick() {
                this.listQuery.date_gte = format(new Date(this.datefilter[0]), 'YYYY-MM-DD');
                this.listQuery.date_lte = format(new Date(this.datefilter[1]), 'YYYY-MM-DD');
                this.fetchData();
            },
            handleSizeChange(val) {
                this.listQuery.limit = val;
                this.fetchData();
            },
            handleCurrentChange(val) {
                this.listQuery.offset = val - 1;
                this.fetchData();
            },
            handleSelect(val, row) {
                Array.prototype.indexOf = function (val) {
                    for (var i = 0; i < this.length; i++) {
                        if (this[i] == val) return i;
                    }
                    return -1;
                };
                Array.prototype.remove = function (val) {
                    var index = this.indexOf(val);
                    if (index > -1) {
                        this.splice(index, 1);
                    }
                };
                if (val.length) {
                    if (this.selectId.indexOf(row.id) == -1) {
                        this.selectId.push(row.id);
                    } else {
                        this.selectId.remove(row.id);
                    }
                    this.butstatus = false;
                } else {
                    this.butstatus = true;
                }
            },
            deleteForm() {
                console.log(this.selectId);
                for (var i = 0, len = this.selectId.length; i < len; i++) {
                    deleteUpload(this.selectId[i]).then(response => {
                        delete this.selectId[i]
                    })
                }
                setTimeout(this.fetchData, 3000);
            },
        }
    }
</script>

<style lang='scss'>
    .head-lavel {
        padding-bottom: 50px;
    }

    .table-button {
        padding: 10px 0;
        float: left;
    }

    .table-search {
        float: right;
        padding: 10px 0;
    }

    .table-pagination {
        padding: 10px 0;
        float: right;
    }
</style>