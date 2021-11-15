<template>
    <div>
      <Navbar/>
        <b-card class="mt-4">
            <div class="content-detail-content-info">
                <div class="content-detail-content-info-left">
                    <h4 class="w-100">{{title}}</h4>
                </div>
                <div class="content-detail-content-info-right">
                    <div class="content-detail-content-info-right-user">
                        글쓴이 : {{user}}
                    </div>
                    <div class="content-detail-content-info-right-created">
                        작성일 : {{created}}
                    </div>
                </div>
            </div>
            <div class="content-detail-content pt-5 pl-5 pr-5 pb-5">
                {{context}}
            </div>
            <!-- <div class="content-detail-button">
                <b-button variant="primary">수정</b-button>
                <b-button variant="success">삭제</b-button>
            </div> -->
            <div class="content-detail-comment">
                <CommentList></CommentList>
            </div>
        </b-card>
    </div>
</template>

<script>
import CommentList from '@/components/BoardPage/CommentList.vue'
import axios from 'axios'
import Navbar from '@/components/MainPage/Navbar.vue'

export default {
    name: "ContentDetail",
    components:{
        CommentList,
        Navbar
    },
    data(){
        return{
            title : '',
            user : '',
            created : '',
            context : '',
            pid : window.location.pathname.split("/")[2]

        };
    },
    created(){
        axios({
            method: 'get',
            url: `https://k5a405.p.ssafy.io/backend/post`,
            params : {
                pid : this.pid
            }
        }).then((res) => {
            console.log(res)
            this.title = res.data.title
            this.user = res.data.user_id
            this.created = res.data.create_date
            this.context = res.data.content
        }).catch((err) => {
            alert(err)
        })
    },
    methods:{
    }
}
</script>

<style scoped>
div{
    background-color: black;
}
.content-detail-content-info {
    border: 1px solid white;
    display: flex;
    justify-content: space-between;
}

.content-detail-content-info-left {
    width: 720px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    text-align: center;
    padding: 1rem;
}

.content-detail-content-info-right {
    width: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 1rem;
}

.content-detail-content {
    border: 1px solid white;
    margin-top: 1rem;
    padding-top: 1rem;
    min-height: 720px;
}

.content-detail-button {
    border: 1px solid white;
    margin-top: 1rem;
    padding: 2rem;
}

.content-detail-comment {
    border: 1px solid white;
    margin-top: 1rem;
    padding: 2rem;
}
</style>
