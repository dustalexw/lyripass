<template>
  <aside class="glass-panel lyric-inspector">
    <div class="inspector-header">
      <span class="studio-kicker">WORDS · IN TIME</span><span class="live-dot" />
    </div>
    <template v-if="playingTrack">
      <div class="inspector-record"><MusicNote /></div>
      <h2>{{ playingTrack.title }}</h2>
      <p class="inspector-artist">
        {{ playingTrack.artist_name }}<br /><span>{{ playingTrack.album_name }}</span>
      </p>
      <div class="inspector-lyrics">
        <template v-if="parsed.syncedLines.length"
          ><button
            v-for="(line, i) in parsed.syncedLines"
            :key="i"
            :class="{ 'line-current': isCurrent(line, i) }"
            @click="seek(line.start_ms / 1000)"
          >
            {{ line.text }}
          </button></template
        >
        <p v-else-if="parsed.plainLyrics" class="whitespace-pre-wrap">{{ parsed.plainLyrics }}</p>
        <div v-else class="inspector-missing">
          <MusicNote />
          <h3>{{ playingTrack.instrumental ? 'Just the music.' : 'The words are waiting.' }}</h3>
          <p>
            {{
              playingTrack.instrumental
                ? 'This track is marked as instrumental.'
                : 'Find a match on LRCLIB or add your own lyrics.'
            }}
          </p>
        </div>
      </div>
      <div class="inspector-actions">
        <button class="plate-button" @click="searchLyrics(playingTrack)">
          <Search /> Find lyrics</button
        ><button class="plate-button" @click="editTrack"><Pencil /> Edit</button>
      </div>
    </template>
    <div v-else class="inspector-empty">
      <div class="empty-wave">
        <i
          v-for="(h, i) in [18, 34, 52, 76, 48, 88, 64, 40, 56, 28, 16]"
          :key="i"
          :style="{ height: h + 'px' }"
        />
      </div>
      <h2>A little closer<br />to the music.</h2>
      <p>Play a track to see its lyrics,<br />find a match, or make it your own.</p>
      <span class="studio-chip">Your collection. Your words.</span>
    </div>
    <div class="inspector-footer"><span class="live-dot" /> Lyrics powered by LRCLIB</div>
  </aside>
</template>
<script setup>
import { computed } from 'vue'
import MusicNote from '~icons/mdi/music-note-outline'
import Search from '~icons/mdi/text-search'
import Pencil from '~icons/mdi/pencil-outline'
import { usePlayer } from '@/composables/player.js'
import { useSearchLyrics } from '@/composables/search-lyrics.js'
import { useEditLyricsV2 } from '@/composables/edit-lyrics-v2.js'
import { parseLyricsfile } from '@/utils/lyricsfile.js'
const { playingTrack, progress, seek } = usePlayer()
const { searchLyrics } = useSearchLyrics()
const { editLyricsV2 } = useEditLyricsV2()
const parsed = computed(() => parseLyricsfile(playingTrack.value?.lyricsfile))
const isCurrent = (line, index) => {
  if (!Number.isFinite(line.start_ms)) return false
  const end = Number.isFinite(line.end_ms)
    ? line.end_ms
    : (parsed.value.syncedLines[index + 1]?.start_ms ?? Infinity)
  return progress.value * 1000 >= line.start_ms && progress.value * 1000 < end
}
const editTrack = () => {
  const track = playingTrack.value
  editLyricsV2({
    audioSource: { type: 'library', ...track },
    lyricsfile: { id: track.lyricsfile_id ?? null, content: track.lyricsfile ?? '' },
    trackId: track.id,
  })
}
</script>
