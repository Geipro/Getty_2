<template>
    <div class="board text-center container">
        <h1 class="mb-5">자유게시판</h1>
        <b-table dark striped hover bordered :items="items" :per-page="perPage" :current-page="currentPage" :fields="fields" @row-clicked="rowClick"></b-table>
        <b-pagination v-model="currentPage" :total-rows="rows" :per-page="perPage" align="center"></b-pagination>
        <div class="mt-5 mb-4 flow-row float-right justify-content-end" >
            <b-button variant="primary" class="" @click="write">글쓰기</b-button>
        </div>
    </div>
</template>

<script>
import data from '@/data'

let items = data.Content.sort((a, b) => {return b.content_id - a.content_id})
items = items.map(contentItem => {return {...contentItem, user_name: data.User.filter(userItem => userItem.user_id === contentItem.user_id)[0].name}})

export default {
    name: 'BoardList',
    data (){
        return{
            currentPage : 1,
            perPage : 10,
            fields: [
                {
                    key: 'content_id',
                    label : '번호',
                    sortable: false
                },
                {
                    key: 'title', 
                    label : '제목',
                    sortable: false
                },
                {
                    key: 'user_name',
                    label: '글쓴이',
                    sortable: false
                },
                {
                    key:'created_at',
                    label:'생성일',
                    sortable: false,
                }
            ],
            items : items
        }
    },
    methods:{
        rowClick(item){
            this.$router.push({
                path: `/boardDetail/${item.content_id}`
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
            return this.items.length;
        }
    }
}
</script>
