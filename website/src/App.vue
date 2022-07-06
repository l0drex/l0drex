<template>
  <HeaderBar/>
  <MainContent></MainContent>
  <FooterBar/>
</template>

<script>
import HeaderBar from "@/components/HeaderBar.vue"
import MainContent from "@/components/MainContent";
import FooterBar from "@/components/FooterBar";
import feather from "feather-icons";

export default {
  name: 'App',
  components: {
    HeaderBar,
    MainContent,
    FooterBar
  },
  mounted() {
    feather.replace();
  }
}
</script>

<style>
:root {
  --foreground: black;
  --backgroud: white;
}

body {
  margin: 0;
  padding: 0;
}

#app {
  color: var(--foreground);
  background: var(--background);
  font-family: sans-serif;
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  flex-direction: column;
}

@media (prefers-color-scheme: light) {
  :root {
    --background: #fff9db;
    --foreground: #312b1a;
  }
}

@media (prefers-color-scheme: dark) {
  :root {
    --background: #08161e;
    --foreground: white;
  }
}

a {
  color: var(--foreground);
}
</style>
