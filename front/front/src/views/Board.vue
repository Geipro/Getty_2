<template>
    <div class="board conatiner-fluid h-100">
        <div class="row justify-content-center align-items-center h-100">
            <board-list v-if="Blist"
            ></board-list>

            <board-create v-if="Bcreate"
            ></board-create>

            <board-detail v-if="Bdetail"
            ></board-detail>
        </div>
    </div>
</template>


<script>
import BoardCreate from '@/components/BoardPage/BoardCreate.vue'
import BoardDetail from '@/components/BoardPage/BoardDetail.vue'
import BoardList from '@/components/BoardPage/BoardList.vue'

export default {
    name:'Board',
    components: {
        BoardCreate,
        BoardDetail,
        BoardList
    },
    data(){
        return{
            Bcreate:false,
            Bdetail:false,
            Blist:true
        }
    },
    methods : {

    }
}
</script>