<template>
    <div>
        <el-card>
            <div class="head-lavel">
                <div class="table-button">
                    <el-button type="info" icon="plus" @click="addForm=true">新建值班记录</el-button>
                </div>
                <div class="table-search">
                    <el-input @keyup.enter.native="handleFilter" style="width: 110px;" class="filter-item"
                              placeholder="值班人员"
                              v-model="listQuery.username__contains" icon="circle-close"
                              :on-icon-click="handleIconClick">
                    </el-input>
                    <el-select clearable style="width: 90px" class="filter-item" v-model="listQuery.shift"
                               placeholder="班次">
                        <el-option v-for="item in shiftOptions" :key="item.value" :label="item.key" :value="item.value">
                        </el-option>
                    </el-select>
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
                <el-table :data="tableData" @selection-change="handleSelectionChange" border style="width: 100%">
                    <el-table-column type="selection"></el-table-column>
                    <el-table-column prop='username' label='用户名' sortable></el-table-column>
                    <el-table-column prop='shift' label='班次' sortable>
                        <template scope="scope">
                            <div slot="reference" class="name-wrapper" style="text-align: center">
                                <el-tag :type="shiftOptions[scope.row.shift].type">
                                    {{shiftOptions[scope.row.shift].key}}

                                </el-tag>
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column prop='content' label='值班内容'>
                        <template scope="scope">
                            <span @click="bigContent(scope.row.content)">{{scope.row.content}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop='images' label='截图'>
                        <template scope="scope">
                            <div v-for="item in scope.row.images" :key="item">
                                <img :src="'http://127.0.0.1:8000/upload' + item" height="50"
                                     @click="bigPhoto('http://127.0.0.1:8000/upload' + item)">
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column prop='create_time' label='创建时间' sortable>
                        <template scope="scope">
                            <span>{{scope.row.create_time | parseDate}}</span>
                        </template>
                    </el-table-column>
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
        <el-dialog :visible.sync="addForm" size="larger">
            <add-duty :shiftOptions="shiftOptions" @DialogStatus="getDialogStatus"></add-duty>
        </el-dialog>
        <el-dialog :visible.sync="showPhoto" size="small">
            <img :src="photo" class="photo-align">
        </el-dialog>
        <el-dialog :visible.sync="showContent" size="small">
            <p class="content-align">{{content}}</p>
        </el-dialog>
    </div>
</template>

<script>
    import {getDutyList, deleteDuty, getUploadList} from 'api/tool'
    import {LIMIT} from '@/config'
    import addDuty from './addduty.vue'
    import format from '@/utils/dateformat'
    export default {
        components: {addDuty},
        data() {
            return {
                tableData: [],
                tabletotal: 0,
                searchdata: '',
                photo: '',
                content: '',
                images: [],
                pagesize: [10, 25, 50, 100],
                addForm: false,
                showPhoto: false,
                showContent: false,
                rowdata: {},
                selectId: [],
                butstatus: true,
                listQuery: {
                    offset: 0,
                    limit: LIMIT,
                    username__contains: '',
                    shift: '',
                    time_lte: '',
                    time_gte: '',
                },
                parms: {},
                datefilter: [],
                shiftOptions: {
                    'M': {"key": "早班", "type": "success", "value": "M"},
                    'A': {"key": "中班", "type": "primary", "value": "A"},
                    'N': {"key": "晚班", "type": "danger", "value": "N"}
                },
            }
        },
        computed: {},
        created() {
            this.fetchData();
        },
        methods: {
            fetchData() {
                getDutyList(this.listQuery).then(response => {
                    this.tableData = response.data.results;
                    this.tabletotal = response.data.count;
                })
            },
            getDialogStatus(data) {
                this.addForm = data;
                this.fetchData();
            },
            handleSelectionChange(val) {
                this.selectId = [];
                for (var i = 0, len = val.length; i < len; i++) {
                    this.selectId.push(val[i].id);
                }
                if(this.selectId.length>0){
                    this.butstatus = false
                } else {
                    this.butstatus = true
                }
            },
            handleIconClick() {
                this.listQuery.username__contains = ''
            },
            searchClick() {
                this.listQuery.time_gte = format(new Date(this.datefilter[0]), 'YYYY-MM-DD');
                this.listQuery.time_lte = format(new Date(this.datefilter[1]), 'YYYY-MM-DD');
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
            deleteForm() {
                for (var i = 0, len = this.selectId.length; i < len; i++) {
                    deleteDuty(this.selectId[i]).then(response => {
                        delete this.selectId[i]
                    })
                }
                setTimeout(this.fetchData, 3000);
            },
            showImg(id) {
                getUploadList(this.parms, id).then(res => {
                    console.log(res.data.file);
                    return res.data.file
                });
            },
            bigPhoto(img) {
                this.showPhoto = true;
                this.photo = img
            },
            bigContent(content) {
                this.showContent = true;
                this.content = content
            }
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
    .photo-align {
        clear: both;
        display: block;
        margin: auto;
    }
    .content-align {
        text-align: center;
    }
    .showimg {
        padding: 1px 10px;
    }
</style>