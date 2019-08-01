<template>
  <div class="listings">
    <div 
      v-for="listing in listings"
      class="listing" 
      :class="{'active': listing == selectedListing}"
      :key="listing.id"
      @click="selectListing(listing)">
      <div class="images">
        <img src="@/assets/carHeader.jpg"/>
      </div>
      <div class="text">
        <div class="header">
          <h2>{{listing.header}}</h2>
          <h3>{{listing.make_name}} {{listing.model_name}} {{listing.year}}</h3>
        </div>
        <div class="content">
          <h1>${{listing.price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}}</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang='scss'>
.listings{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  .listing{
    cursor: pointer;
    width: calc(100% - 1rem);
    max-width: 700px;
    height: 33vh;
    margin: 1rem .5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: .5rem;
    background: radial-gradient(circle at top left, rgba(64,63,63,1) 0%, rgba(39,39,39,1) 53%, rgba(34,34,34,1) 93%);
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
    transition: all .5s ease-in-out;
    height: 20rem;
    &.active{
      height: calc(100vh - 4.5rem);
    }
    .images{
      max-width: 50%;
      height: 85%;
      img{
        max-width:100%;
        height: 100%;
        border-radius: .5rem;
        margin-left: -1.5rem;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
      }
    }
    .text{
      max-width: 60%;
      padding: 1rem;
      margin: auto;
      .header{
        width: 100%;
        h2{
          border-bottom: 1px solid white;
          font-size: 1.75rem;
          padding: .5rem;
        }
        h3{
          padding: .5rem;
        }
      }
      .content{
        width: 80%;
        display: flex;
        justify-content: center;
        align-content: center;
        flex-wrap: wrap;
        margin: 1rem auto;
        h1{
          margin: .5rem;
          padding: .5rem 1rem;
          border-radius: 5rem;
          border: 1px solid #ca1b1b;
          color: white;
        }
      }
    }
  }
}
</style>

<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: 'home',
  data (){
    return{
      listings: [],
      selectedListing: null,
    }
  },
  created(){
    this.$http.get('vehicles/').then((response) =>{
      this.listings=response.data
    })
  },
  methods:{
    selectListing(listing){
      if(listing){
        this.selectedListing = listing
      }
    }
  }

}
</script>
