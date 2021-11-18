<template>
    <div class="comment-create">
        <b-input-group class="mt-3">
            <b-form-textarea
                id="textarea"
                v-model="comment.content"
                :placeholder="'코멘트를 달아주세요~!'"
                rows="2"
                max-rows="2"
            ></b-form-textarea>
            <b-input-group-append>
                <b-button class="btn-lg" variant="info" @click="createComment()">작성하기</b-button>
            </b-input-group-append>
        </b-input-group>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: "CommentCreate",
    data() {
        return {
            comment:{
                content : "",
                create_date : "",
            }
        };
    },
    created(){
        let today = new Date();
        this.comment.create_date = today.toLocaleDateString() + " " + today.getFullYear() + ":" + today.getHours() + ":" + today.getMinutes();
    },
    methods: {
        createComment() {
            axios({
                method:'post',
                url:`https://k5a405.p.ssafy.io/backend/comment`,
                params:{
                    pid : window.location.pathname.split("/")[2]
                },
                headers:{
                    token : localStorage.getItem("Token")
                },
                data : this.comment
            }).then((res) => {
                //console.log(res)
                res
                this.$router.go();
            }).catch((err) => {
                //alert(err)
                err
            })
        },
    }
};
</script>

<style scoped>
.comment-create {
    display: flex;
    margin-bottom: 1em;
}
</style>
