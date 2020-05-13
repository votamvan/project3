import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home.vue'
import MainApp from './components/MainApp.vue'
import About from './components/About.vue'


Vue.use(Router)

export default new Router({
	mode: 'history',
	routes:[
		{
			path:'/',
			name:'Home',
			component:Home
		},
		{
			path:'/main-app',
			name:'MainApp',
			component:MainApp
		},
		{
			path:'/about',
			name:'About',
			component:About
		}
	],
	duplicateNavigationPolicy: 'reload'
}) 