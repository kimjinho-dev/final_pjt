<template>
  <b-container style="width:726px">
    <h1>MoviesView</h1>
    <MovieSearch/>
    <MovieToprated/>
    <MovieRandomGenre/>
  </b-container>
</template>

<script>
import MovieToprated from '@/components/movies/MovieToprated'
import MovieRandomGenre from '@/components/movies/MovieRandomGenre'
import MovieSearch from '@/components/movies/MovieSearch'

export default {
  components: {
    MovieToprated,
    MovieRandomGenre,
    MovieSearch,
  }
}
</script>

<style>
</style>