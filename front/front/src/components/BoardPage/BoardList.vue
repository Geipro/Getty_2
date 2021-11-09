<template>
    <div class="board text-center container">
        <h1 class="mb-5">자유게시판</h1>
        <b-table dark striped hover bordered :items="items" :per-page="perPage" :current-page="currentPage" :fields="this.fields" @row-clicked="rowClick"></b-table>
        <b-pagination v-model="currentPage" :total-rows="rows" :per-page="perPage" align="center"></b-pagination>
        <div class="mt-5 mb-4 flow-row float-right justify-content-end" >
            <b-button variant="primary" class="" @click="write">글쓰기</b-button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'BoardList',
    data (){
        return{
            currentPage : 1,
            perPage : 10,
            fields: [
                {
                    key: 'pid',
                    label : '번호',
                    sortable: false
                },
                {
                    key: 'title', 
                    label : '제목',
                    sortable: false
                },
                {
                    key: 'user_id',
                    label: '글쓴이',
                    sortable: false
                },
                {
                    key:'create_date',
                    label:'생성일',
                    sortable: false,
                }
            ],
            boards: [],
            items : []
        }
    },
    created() {
        axios({
            method: 'get',
            url: `https://k5a405.p.ssafy.io/backend/posts`,
        }).then((res) => {
            console.log(res)
            this.boards = res.data
            this.items = this.boards.sort((a, b) => {return b.pid - a.pid})
        }).catch((err) => {
            alert(err)
        })
    },
    methods:{
        rowClick(item){
            this.$router.push({
                path: `/boardDetail/${item.pid}`
            })
        },
        getList(){
            //axios
        },
        write(){
            this.$router.push({
                path:'/boardCreate'
            })
        }
    },
    computed:{
        rows(){
            return this.boards.length;
        }
    }
}
</script>
