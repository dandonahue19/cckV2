<template>
  <div class="listings">
    <div class="listing" v-for="listing in listings" :key="listing.id">
      <div class="images">
        <img src="@/assets/carHeader.jpg"/>
      </div>
      <div class="text">
        <div class="header">
          <h2>{{listing.header}}</h2>
          <h3>{{listing.make}} {{listing.model}} {{listing.year}}</h3>
        </div>
        <div class="content">
          <div class="info-item">
            <h3>Drive :</h3>
            <h3>{{listing.drive}}</h3>
          </div>
          <div class="info-item">
            <h3>Transmission :</h3>
            <h3>{{listing.transmission}}</h3>
          </div>
          <div class="info-item">
            <h3>Fuel :</h3>
            <h3>{{listing.fuel}}</h3>
          </div>
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
    width: calc(100% - 1rem);
    max-width: 700px;
    height: 33vh;
    margin: 1rem .5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #272727;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
    .images{
      max-width: 50%;
      height: 100%;
      overflow: hidden;
      img{
        max-width:100%;
        height: 100%;
      }
    }
    .text{
      max-width: 50%;
      height:100%;
      padding: 1rem;
      margin: auto;
      .header{
        width: 100%;
        h2{
          border-bottom: 1px solid white;
        }
      }
      .content{
        width: 80%;
        display: flex;
        justify-content: center;
        align-content: center;
        flex-wrap: wrap;
        margin: 1rem auto;
        .info-item{
          display: flex;
          justify-content: center;
          width: 100%;
          opacity: .8;
          h3{
            width: 50%;
            margin: .25rem .5rem;
            &:first-child{
              text-align: right;
            }
          }
        }
        h1{
          margin: .5rem;
          padding: .5rem 1rem;
          border-radius: 5rem;
          background-color: #ca1b1b;
          color: white;
        }
      }
    }
  }
}
</style>

<script>
// @ is an alias to /src

export default {
  name: 'home',
  data (){
    return{
      listings: [{
        image: '/img/carHeader.jpg',
        header: 'Low Mileage, Fleet Maintained',
        price: 6000,
        make: 'Ford',
        model: 'Tarus',
        year: 2009,
        mileage: 46000,
        drive: 'AWD',
        fuel:'Gas',
        transmission:'Automatic'
      },{
        image: '/img/carHeader.jpg',
        header: 'Low Mileage, Fleet Maintained',
        price: 6000,
        make: 'Ford',
        model: 'Tarus',
        year: 2009,
        mileage: 46000,
        drive: 'AWD',
        fuel:'Gas',
        transmission:'Automatic'
      }]
    }
  }

}
</script>
