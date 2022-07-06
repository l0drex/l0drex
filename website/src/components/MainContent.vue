<template>
  <main>
    <div id="welcome">
      <h1>Welcome to my Homepage!</h1>
      <p>I'm a computer science student from Dresden, Germany.<br>
        I love to explore technology, so I have started a lot of cool projects in my freetime.</p>
      <p>Check them out below!</p>
    </div>

    <article>
      <h1 id="Projects"><i data-feather="code"></i> Projects</h1>
      <p>
        As you can see from my <a href="https://github.com/l0drex?tab=repositories">GitHub repositories</a>,
        I love to try out a lot of languages and frameworks:
      </p>
      <section class="card-row">
        <CardItem title="Homepage"
                  description="The website you currently see."
                  link="https://github.com/l0drex/l0drex/website"
                  :tags="['HTML', 'CSS', 'Vue', 'Javascript']"/>
        <CardItem title="Family Tree"
                  description="Visualizes genealogy data from GedcomX files."
                  link="https://github.com/l0drex/family-tree"
                  :tags="['HTML', 'CSS', 'React', 'Typescript', 'd3']"/>
        <CardItem title="Wallpaper Splitter"
                  description="Apply an image as your wallpaper, crossing all your monitors."
                  link="https://github.com/l0drex/WallpaperSplitter"
                  :tags="['C++', 'CMAKE', 'Qt', 'KDE']"/>
        <CardItem title="Intellij Breeze Theme"
                  description="Brings KDE Plasmas Breeze theme to Intellij IDEs."
                  link="https://github.com/l0drex/Intellij-KDE-Breeze-Theme"
                  :tags="['gradle', 'Python', 'XML', 'JSON']"/>
      </section>

      <p>
        I also help with other open source projects:
      </p>
      <section class="card-row">
        <CardItem title="Yin Yang"
                  description="Automatic night theme on Linux"
                  link="https://github.com/oskarsh/Yin-Yang"
                  :tags="['Python']"/>
        <CardItem title="auto-dark-mode"
                  description="Automatic night theme in Intellij IDEs"
                  link="https://github.com/weisJ/auto-dark-mode"
                  :tags="['Kotlin', 'Java']"/>
      </section>
    </article>

    <article>
      <h1 id="Contact"><i data-feather="users"></i> Contact</h1>
      <ul class="contacts">
        <li><i data-feather="mail" />
          <a href="mailto:hoffmann_lorenz@protonmail.com">hoffmann_lorenz@protonmail.com</a></li>
        <li><i data-feather="phone" />
          <a href="tel:+49 1573 2259591">+49 1573 2259591</a></li>
      </ul>
    </article>
  </main>
</template>

<script>
import CardItem from "@/components/CardItem";

export default {
  name: "MainContent",
  components: {CardItem}
}
</script>

<style scoped>
main {
  flex-grow: 1;
}

article {
  margin: 2rem 0;
}

article > * {
  margin-left: max(1rem, 10%);
  margin-right: max(1rem, 10%);
}

#welcome {
  text-align: center;
  padding: 3rem;
}

.card-row {
  display: flex;
  overflow-x: scroll;
  gap: 1rem;
}

.contacts {
  list-style: none;
}

.contacts .feather {
  margin-right: .5em;
}
</style>