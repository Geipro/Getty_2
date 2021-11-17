<template>
    <div v-if="!isLogin" class="container text-center">
        <h1>로그인을 해주세요!</h1>
    </div>
    <div v-else class="container">
        <div class="inline-block mb-2">
            <a class="mt-3 mb-4 float-left text-left offset-4" style="font-size: 30px">커뮤니티</a>
        </div>
        <b-table class="text-center" dark striped hover bordered 
        :items="items" :per-page="perPage" :current-page="currentPage" 
        :fields="this.fields" @row-clicked="rowClick" style="width:900px" align="center"></b-table>
        <b-pagination class="text-center" v-model="currentPage" :total-rows="rows" :per-page="perPage" align="center"></b-pagination>
        <div class="mt-5 mb-4 text-center" >
            <b-button variant="primary" class="" @click="write">글쓰기</b-button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'BoardList',
    components: {
    },
    data (){
        return{
            currentPage : 1,
            isLogin:false,
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
    mounted(){
        if(localStorage.getItem("Token") != null){
            this.isLogin = true;
        }
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
