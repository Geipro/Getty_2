<template>
    <div>
        <div :key="item.comment_id" v-for="item in comments">
            <CommentListItem :commentObj="item"></CommentListItem>
        </div>
        <CommentCreate :contentId="contentId" :reloadComment="reloadComment"/>
    </div>
</template>

<script>
import data from "@/data";
import CommentListItem from "./CommentItem";
import CommentCreate from "./CommentCreate";
import axios from "axios"

export default {
    name: "CommentList",
    props: {
        contentId: Number
    },
    data() {
        return {
            comments: data.Comment.filter(commentItem => {
                return commentItem.content_id === this.contentId;
            })
        };
    },
    components: {
        CommentListItem,
        CommentCreate
    },
    created(){
        axios({
            method:'get',
            url: `https://k5a405.p.ssafy.io/backend/comment`,
            data: this.pid
        }).then(res => {
            
            console.log(res)
        })
    },
    methods: {
        reloadComment() {
            this.comments = data.Comment.filter(commentItem => {
                return commentItem.content_id === this.contentId;
            });
        }
    }
};
</script>

<style>
</style>