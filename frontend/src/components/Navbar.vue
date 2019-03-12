<template>
<div class="navbar">
    <router-link  v-for="page in pages" 
        :key="page.name"
        :to="{name: page.route}" 
        tag='div'
        class="page">
        {{page.name}}
    </router-link>
</div>
</template>

<style lang='scss'>
.navbar{
    display: flex;
    justify-content: center;
    z-index: 99;
    .page{
        width: 30%;
        max-width: 10rem;
        margin: 1rem;
        padding: .5rem 1.5rem;
        border-radius: 3.25rem;
        text-align: center;
        color: white;
        text-decoration: none;
        text-shadow: -1px 2px 3px black;
        &.active{
            background-color: #ca1b1b;
            box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)
        }
    }
}
</style>

<script>

export default{
    data(){
        return{
            pages:[
                {
                    route: 'home',
                    name: 'HOME'
                },
                {
                    route: 'listings',
                    name: 'AVAILABLE'
                },
                {
                    route: 'contact',
                    name: 'CONTACT'
                },
            ]
        }
    },
    methods:{
        
    }
}

</script>