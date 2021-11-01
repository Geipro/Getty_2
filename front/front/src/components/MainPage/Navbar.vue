<template>
  <div style="color: white" class="justify-content-center bg-dark">
    <router-link :to="{ name: 'Home' }">
      <img src="@/assets/logo.png" style="width:70px">
    </router-link>
    Getty
    <!-- 로고 옆으로 조정해보기 -->
    <!-- <div class="justify-content-end ">
      <router-link :to="{ name: 'About' }" class=" nav-link">로그인</router-link>
    </div> -->
  <nav class="navbar sticky-top navbar-expand-lg navbar-success bg-dark" id="navbar">
  <div class="container-fluid">
    <div class="collapse navbar-collapse" id="navbarNav">
      <span v-if="isLogin">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link :to="{ name: 'Mypage' }" class="text-light nav-link">마이페이지</router-link>
          </li>
          <li class="nav-item">
            <router-link @click.native="logout" to="#" class="text-light nav-link" text-decoration: none>로그아웃</router-link>
          </li>
        </ul>
      </span>
      <span v-else>
        <ul class="nav">
          <!-- <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="http://localhost:8080/loanList" style="color: white">금융서비스</a>
          </li> -->
          <!-- <li class="nav-item">
            <router-link :to="{ name: 'About' }" class="text-light nav-link">로그인</router-link>
          </li> -->
        </ul>
      </span>
    </div>
    <div class="container-fluid justify-content-center">
      <ul class="nav nav-pills">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Active</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Dropdown</a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Separated link</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
    </div>
  </div>
  <br>
</nav>
</div>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    msg: String
  },
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('Token')
      localStorage.removeItem('ID')
      this.$router.go()
    },
  },
  created: function () {
    const token = localStorage.getItem('Token')
    if (token != null) {
      this.isLogin = true
    }
  }
}
</script>

<style scoped>
/* h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */

/* #navbar {
  font-family: 'Noto Sans KR', sans-serif;
} */

</style>
