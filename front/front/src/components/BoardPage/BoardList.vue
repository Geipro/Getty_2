<template>
    <div class="board text-center container">
        <h1 class="mb-5">자유게시판</h1>
        <b-table dark striped hover bordered :items="items" :fields="fields"></b-table>
		<!-- <b-table class="table table-dark table-striped table-bordered table-hover col-md-12 text-center text-light">
			<colgroup>
				<col style="width:10%">
				<col style="width:*">
				<col style="width:15%">
				<col style="width:25%">
			</colgroup>
			<thead>
				<tr>
					<th scope="col">번호</th>
					<th scope="col">제목</th>
					<th scope="col">작성자</th>
					<th scope="col">작성일</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="boardItem in this.boardList" v-bind:key="boardItem.no">
					<td>{{boardItem.no}}</td>
					<td>{{boardItem.subject}}</td>
					<td>{{boardItem.writer}}</td>
					<td>{{boardItem.writedate}}</td>
				</tr>
			</tbody>
		</b-table> -->
        <div class="mt-5 mb-4 flow-row float-right justify-content-end" >
            <b-button variant="primary" class="" @click="write">글쓰기</b-button>
        </div>
    </div>
</template>

<script>
import data from '@/data'
export default {
    name: 'BoardList',
    data (){
        return{
            items: data.Content,
            fields: [
                {
                    key: 'content_id',
                    label : '번호',
                    sortable: true
                },
                {
                    key: 'title', 
                    label : '제목',
                    sortable: false
                },
                {
                    key:'created_at',
                    label:'생성일',
                    sortable: false,
                }
            ],
            boardList:[
                {
                    "no": 1,
                    "subject": "테스트 제목1",
                    "content": "테스트 내용1",
                    "writer": "testid1",
                    "writedate": "2021-08-09 13:00:00"
                },
                {
                    "no": 2,
                    "subject": "테스트 제목2",
                    "content": "테스트 내용2",
                    "writer": "testid2",
                    "writedate": "2021-08-09 13:10:00"
                },
                {
                    "no": 3,
                    "subject": "테스트 제목3",
                    "content": "테스트 내용3",
                    "writer": "testid3",
                    "writedate": "2021-08-09 13:20:00"
                },
                {
                    "no": 4,
                    "subject": "테스트 제목4",
                    "content": "테스트 내용4",
                    "writer": "testid4",
                    "writedate": "2021-08-09 13:20:50"
                },
                {
                    "no": 5,
                    "subject": "테스트 제목5",
                    "content": "테스트 내용5",
                    "writer": "testid5",
                    "writedate": "2021-08-09 13:30:50"
                },
                {
                    "no": 6,
                    "subject": "테스트 제목6",
                    "content": "테스트 내용6",
                    "writer": "testid6",
                    "writedate": "2021-08-09 13:45:50"
                }
            ]
        }
    },
    methods:{
        getList(){
            //axios
        },
        write(){
            this.$router.push({
                path:'/boardCreate'
            })
        }
    }
}
</script>
