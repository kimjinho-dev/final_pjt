<template>
  <b-container style="width:726px">
    <h1>MoviesView</h1>
    <MovieSearch/>
    <MoviePopular/>
    <MovieRandomGenre/>
  </b-container>
</template>

<script>
import MoviePopular from '@/components/movies/MoviePopular'
import MovieRandomGenre from '@/components/movies/MovieRandomGenre'
import MovieSearch from '@/components/movies/MovieSearch'

export default {
  components: {
    MoviePopular,
    MovieRandomGenre,
    MovieSearch,
  }
}
</script>

<style>
</style>