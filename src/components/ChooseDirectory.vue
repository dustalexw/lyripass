<template>
  <main class="setup-page">
    <section class="setup-story">
      <span class="studio-kicker">YOUR MUSIC. EVERY WORD.</span>
      <h1>A home for<br />your music’s <em>lyrics.</em></h1>
      <p>Bring your collection. Find the words. Keep everything in time.</p>
      <div class="setup-features">
        <div>
          <span class="feature-number">01</span>
          <div>
            <strong>Connect your collection</strong>
            <p>Choose a local folder or a mounted music drive.</p>
          </div>
        </div>
        <div>
          <span class="feature-number">02</span>
          <div>
            <strong>Find the right lyrics</strong>
            <p>Download synced lyrics from LRCLIB, across your library.</p>
          </div>
        </div>
        <div>
          <span class="feature-number">03</span>
          <div>
            <strong>Make every word yours</strong>
            <p>Fine-tune timings, then export LRC, text, or embedded lyrics.</p>
          </div>
        </div>
      </div>
      <div class="setup-credit">Built on LRCGET <span>·</span> Reimagined as Lyripass</div>
    </section>
    <section class="glass-panel setup-folders">
      <span class="studio-kicker">FROM · YOUR COLLECTION</span>
      <h2>Where does your music live?</h2>
      <p>Add the folders you want Lyripass to scan.</p>
      <div class="directory-list">
        <div v-for="(directory, index) in directories" :key="directory" class="directory-row">
          <Folder class="folder-icon" />
          <div class="directory-path">{{ directory }}</div>
          <button
            class="icon-button"
            :aria-label="`Remove ${directory}`"
            @click="removeDirectory(index)"
          >
            <Close />
          </button>
        </div>
        <button class="add-directory" @click="chooseDirectory"><Plus /> Add music folder</button>
      </div>
      <div class="setup-note">
        <Check /><span>Lyrics stay in Lyripass until you choose to export.</span>
      </div>
      <button
        class="button button-primary setup-continue"
        :disabled="!directories.length"
        @click="progressStep"
      >
        Open my library <ArrowRight />
      </button>
      <span class="setup-formats">MP3 · FLAC · M4A · OGG · and more</span>
    </section>
  </main>
</template>

<script setup>
import { open } from '@tauri-apps/plugin-dialog'
import { audioDir } from '@tauri-apps/api/path'
import { invoke } from '@tauri-apps/api/core'
import { ref, onMounted } from 'vue'
import Close from '~icons/mdi/close'
import Plus from '~icons/mdi/plus'
import Folder from '~icons/mdi/folder-music-outline'
import ArrowRight from '~icons/mdi/arrow-right'
import Check from '~icons/mdi/check'
const emit = defineEmits(['progressStep', 'directoriesChanged'])

const directories = ref([])
const originalDirectories = ref([])

const progressStep = async () => {
  if (!directories.value.length) return
  await invoke('set_directories', { directories: directories.value })

  // Check if directories actually changed
  const hasChanged =
    JSON.stringify(originalDirectories.value.sort()) !== JSON.stringify(directories.value.sort())

  if (hasChanged) {
    emit('directoriesChanged')
  }

  emit('progressStep')
}

onMounted(async () => {
  const directoriesFromDB = await invoke('get_directories')
  if (directoriesFromDB && directoriesFromDB.length > 0) {
    directories.value = [...directoriesFromDB]
    originalDirectories.value = [...directoriesFromDB]
  } else {
    const dirPath = await audioDir()
    directories.value.push(dirPath)
    originalDirectories.value = [dirPath]
  }
})

const chooseDirectory = async () => {
  const selected = await open({
    directory: true,
    recursive: true,
  })

  if (selected && !directories.value.includes(selected)) {
    directories.value.push(selected)
  }
}

const removeDirectory = index => {
  if (index < 0) {
    return
  }
  directories.value.splice(index, 1)
}
</script>
