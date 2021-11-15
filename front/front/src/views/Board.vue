<template>
    <div class="board conatiner-fluid h-100" style="text-align: center;">
      <Navbar/>
      <div class="row justify-content-center align-items-center h-100 mt-4">
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
import Navbar from '@/components/MainPage/Navbar.vue'

export default {
    name:'Board',
    components: {
        BoardCreate,
        BoardDetail,
        BoardList,
        Navbar,
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
