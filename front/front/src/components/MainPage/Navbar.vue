<template>
<div>
  <div class="d-flex justify-content-end">
    <span v-if="isLogin">
      <ul class="ulist" >
        <li>
          <router-link :to="{ name: 'Mywrite' }" class="text-light nav-link mt-3">마이페이지</router-link>
        </li>
        <li>
          <router-link @click.native="logout" to="#" class="text-light nav-link mr-3" text-decoration: none>로그아웃</router-link>
        </li>
      </ul>
    </span>
    <span v-else>
      <ul>
        <li>
          <router-link :to="{ name: 'About' }" class="text-light nav-link mt-3">로그인 / 회원가입</router-link>
        </li>
        <!-- <li>
          <a class="nav-link active" aria-current="page" href="/signup" style="color: white">회원가입</a>
        </li> -->
      </ul>
    </span>
  </div>


  <div class="justify-content-center mb-4 title-style" style="text-align: center;">
    <router-link :to="{ name: 'Home' }">
      <img src="@/assets/logo.png" style="width:70px">
    </router-link>
    Getty
  </div>
  <div>
    <b-navbar type="dark" variant="#2c3e50" class="justify-content-center">
      <b-navbar-nav style="border-bottom:1px solid #ffffff;">
        <!-- Navbar dropdowns -->
        <b-nav-item-dropdown text="금융상품" right class="nav-margin text-light">
          <b-dropdown-item href="/deposit">예금 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b-dropdown-item>
          <b-dropdown-item href="/savings">적금&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b-dropdown-item>
          <b-dropdown-item href="/creditloan">신용대출</b-dropdown-item>
          <b-dropdown-item href="/renthouse">전세자금대출</b-dropdown-item>
          <b-dropdown-item href="/mortgage">주택담보대출</b-dropdown-item>
        </b-nav-item-dropdown>
        <!-- <router-link :to="{ name: 'News' }" class="text-light nav-link">뉴스</router-link> -->

        <b-nav-item href="/news" class="nav-margin text-light">뉴스</b-nav-item>
        <b-nav-item href="/board" class="nav-margin text-light">커뮤니티</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
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
.ulist {
   list-style: none;
}
ul {
  padding: 0;
}
li {
  display: inline-block;
}
.nav-margin{
    padding-right: 6rem;
    padding-left: 6rem;
    /* padding-top: 1rem; */
    color: white;
}
.title-style {
  color: white;
  font-size: 2.5rem;
  background-color: #1f2325;
  /* background-color: #2c3e50; */
}

</style>
