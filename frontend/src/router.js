import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  linkActiveClass: 'active',
  routes: [
    {path: '/home', name: 'home', component: Home},
    
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    {path: '/listings', name: 'listings', component: () => import(/* webpackChunkName: "about" */ './views/Listings.vue')},
    {path: '/contact',  name: 'contact',  component: () => import('./views/Contact.vue')}
  ]
})
