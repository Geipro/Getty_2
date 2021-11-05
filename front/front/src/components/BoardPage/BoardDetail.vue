<template>
    <div>
        <b-card>
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
            <div class="content-detail-content">
                {{context}}
            </div>
            <div class="content-detail-button">
                <b-button variant="primary">수정</b-button>
                <b-button variant="success" @click="deleteData">삭제</b-button>
            </div>
            <div class="content-detail-comment">
                <CommentList :contentId="contentId"></CommentList>
            </div>
        </b-card>
    </div>
</template>

<script>
import data from '@/data'
import CommentList from '@/components/BoardPage/CommentList.vue'

export default {
    name: "ContentDetail",
    components:{
        CommentList
    },
    data(){
        const contentId = Number(this.$route.params.contentId);
        const contentData = data.Content.filter(item => item.content_id === contentId)[0];
        return{
            contentId : contentId,
            title : contentData.title,
            context : contentData.context,
            user : data.User.filter(item => item.user_id === contentData.user_id)[0].name,
            created : contentData.created_at
        };
    },
    methods:{
        deleteData(){
            const content_index = data.Content.findIndex(item => item.content_id === this.contentId);
            data.Content.splice(content_index, 1)
            this.$router.push({
                path : '/board'
            })
        },
        updateData() {
        this.$router.push({
            path: `/board/create/${this.contentId}`
        });
    }
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