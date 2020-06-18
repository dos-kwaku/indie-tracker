<template>
  <div id="app">
    <div class="w-full max-w-xs mx-auto"> 
      <label
        class="block text-gray-700 text-sm font-bold mb-2"
      >Analyze How "Indie" Your Playlist Is</label>
      <input 
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        placeholder="Enter a Spotify playlist URL"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>