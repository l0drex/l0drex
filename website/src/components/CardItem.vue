<template>
  <div class="card">
    <h3><a :href="link">{{ title }} <i data-feather="external-link"/></a></h3>
    <p>{{ description }}</p>
    <ul class="tag">
      <li v-for="tag in tags" v-bind:key="tag">{{tag}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "CardItem",
  props: ["title", "description", "link", "tags"]
}
</script>

<style scoped>
.card {
  background: rgba(128, 128, 128, 0.2);
  border-radius: 1rem;
  padding: 1rem;
  min-width: 13rem;
}

.card h3 {
  margin: 0;
}

.card h3 a {
  text-decoration: none;
}

.tag {
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .3rem;
  font-size: .8em;
  user-select: none;
}

.tag li {
  background: rgba(128, 128, 128, 0.2);
  border-radius: .5em;
  list-style: none;
  padding: 0 .5rem;
  transition: all .3s;
}

.tag li:hover {
  scale: 1.3;
}
</style>