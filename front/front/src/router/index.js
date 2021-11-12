import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Mypage from '@/views/Mypage.vue'
import Mywrite from '@/views/Mywrite.vue'
import Myreview from '@/views/Myreview.vue'
import News from '@/views/News.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/mypage',
    name: 'Mypage',
    component: Mypage
  },
  {
    path: '/mywrite',
    name: 'Mywrite',
    component: Mywrite
  },
  {
    path: '/myreview',
    name: 'Myreview',
    component: Myreview
  },
  {
    path: '/board',
    name: 'Board',
    component: () => import('../views/Board.vue')
  },
  {
    path: '/boardCreate/:contentId?',
    name: 'BoardCreate',
    component: () => import('../components/BoardPage/BoardCreate.vue')
  },
  {
    path: "/boardDetail/:contentId",
    name: "BoardDetail",
    component: () => import('../components/BoardPage/BoardDetail.vue')
  },
  {
    path: '/creditloan',
    name: 'CreditLoan',
    component: () => import('../components/FinanceProduct/CreditLoan.vue')
  },
  {
    path: '/deposit',
    name: 'Deposit',
    component: () => import('../components/FinanceProduct/Deposit.vue')
  },
  {
    path: '/renthouse',
    name: 'RentHouse',
    component: () => import('../components/FinanceProduct/RentHouse.vue')
  },
  {
    path: '/mortgage',
    name: 'Mortgage',
    component: () => import('../components/FinanceProduct/Mortgage.vue')
  },
  {
    path: '/savings',
    name: 'Savings',
    component: () => import('../components/FinanceProduct/Savings.vue')
  },
  {
    path: '/product',
    name: 'Product',
    component: () => import('../views/Product.vue')
  },
  {
    path: '/news',
    name: 'News',
    component: News
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
