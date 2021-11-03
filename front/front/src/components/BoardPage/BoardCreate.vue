<template>
    <div>
        <div class="container mb-5">
            <h2 class="text-left">제목</h2>
            <b-input v-model="subject" placeholder="제목을 입력하시오"></b-input>
        </div>
        <div class="container mb-3">
            <b-form-textarea v-model="context" placeholder="내용을 입력하시오" rows="5" max-rows="10">
            </b-form-textarea>
        </div>
        <b-button variant="primary" class="mr-3" @click="upload ? uploadContent() : updateContent()">저장</b-button> &nbsp;&nbsp;
        <b-button @click="cancel">취소</b-button>
    </div>
</template>

<script>
export default{
    name: 'BoardCreate',
    data(){
        return{
            subject : '',
            context : '',
            
        }
    },
    created(){

    },
    methods:{
        uploadContent(){
            this.$router.push({path:'/board'})
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