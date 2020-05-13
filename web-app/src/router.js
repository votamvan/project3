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
			path:'/MainApp',
			name:'MainApp',
			component:MainApp
		},
		{
			path:'/About',
			name:'About',
			component:About
		}
	],
	duplicateNavigationPolicy: 'reload'
}) 