<template>
    <div>
        <div class="container mb-3">
            <h1 class="border">자유게시판</h1>
        </div>
        <div class="container mb-5">
            <b-input v-model="boardData.title" placeholder="제목을 입력하시오"></b-input>
        </div>
        <div class="container mb-3">
            <b-form-textarea v-model="boardData.content" placeholder="내용을 입력하시오" rows="10" max-rows="10">
            </b-form-textarea>
        </div>
        <b-button variant="primary" class="mr-3" @click="uploadContent()">저장</b-button> &nbsp;&nbsp;
        <b-button @click="cancel">취소</b-button>
    </div>
</template>

<script>
import axios from 'axios'
 

export default{
    name: 'BoardCreate',
    data(){
        return{
            boardData:{
                title : '',
                content : '',
                create_date : ''
            }
        }
    },
    created(){
        let today = new Date();
        this.boardData.create_date = today.toLocaleDateString() + " " + today.getFullYear() + ":" + today.getHours() + ":" + today.getMinutes();
        console.log(this.boardData.create_date)
    },
    methods:{
        uploadContent(){
            axios({
                method: 'post',
                url: `https://k5a405.p.ssafy.io/backend/post`,
                headers:{
                    "token" : localStorage.getItem("Token")
                },
                data : this.boardData
            }).then(res => {
                alert("업로드가 완료되었습니다.")
                this.$router.push({path:'/board'})
                console.log(res)
            }).catch(err => {
                alert(err)
            })
        },
        updateContent(){
            this.$router.push({path:'/board'})
        },
        cancel(){
            this.$router.push({path:'/board'})
        }
    }
}
</script>