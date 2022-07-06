<template>
  <header>
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#Projects">Projects</a></li>
        <li><a href="#Contact">Contact</a></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: "HeaderBar"
}
</script>

<style scoped>
header {
  padding: .5rem 1rem;
}

nav ul {
  list-style: none;
  display: flex;
  margin: 0;
  padding: 0;
  gap: 1rem;
  align-items: baseline;
}

nav li {
  padding: .5rem;
  border-bottom: solid transparent;
  transition: all .3s;
}

nav li:first-child {
  padding: 0;
}

nav a {
  text-decoration: none;
  color: var(--foreground);
  user-select: none;
}

nav li:hover {
  border-bottom: solid var(--foreground);
}

nav li:active {
  background: var(--foreground);
  color: var(--background);
}

nav li:active a {
  color: var(--background);
}
</style>