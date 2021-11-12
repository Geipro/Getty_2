<template>
    <div>
        <div>
            <p></p>
        </div>
        <div :key="item.pid" v-for="item in comments">
            <div v-if="item.content != ''">
                <div class="md-12">
                    <a class="float-left mr-5">{{item.user_id}}</a>
                    <a class="float-right ml-5">{{item.create_date}}</a>
                </div>
                <div class="mt-2">
                    <a>{{item.content}}</a>
                </div>
            </div>
        </div>
        <CommentCreate/>
    </div>
</template>

<script>
import CommentCreate from "./CommentCreate";
import axios from "axios"

export default {
    name: "CommentList",
    props: {
    },
    data() {
        return {
            user_id : '',
            content : '',
            create_date : '',
            comments:[]
        };
    },
    components: {
        CommentCreate
    },
    created(){
        axios({
            method:'get',
            url: `https://k5a405.p.ssafy.io/backend/comment`,
            params:{
                pid : window.location.pathname.split("/")[2]
            }
        }).then((res) => {
            this.comments = res.data
            console.log(res)
        }).catch((err) => {
            alert(err)
        })
    },
    methods: {

    }
};
</script>

<style>
</style>