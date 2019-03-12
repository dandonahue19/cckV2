<template>
  <div class="home">
    <div class="main-picture">
      <img src="@/assets/highway1.jpg"/>
      <h1>Cop Car King</h1>
    </div>
  </div>
</template>

<style lang='scss'>
.home{
  .logo{
    height: 33%;
  }
  .main-picture{
    width: 100%;
    padding: .5rem 1rem;
    h1{
      position: absolute;
      top: 4rem;
      right: 10%;
      font-size: 6rem;
      width: 13rem;
      margin: 0;
      line-height: 5rem;
      opacity: .7;
      text-shadow: -3px 9px 9px rgb(0, 0, 0)
    }
    img{
      width: 100%;
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      margin: auto;
      max-width: 700px;
      opacity: .4;
      box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
    }
  }
}
</style>

<script>
// @ is an alias to /src

export default {
  name: 'home',

}
</script>
