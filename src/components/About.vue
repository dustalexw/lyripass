<template>
  <BaseModal title="About Lyripass" @close="$emit('close')"
    ><div class="about-lyripass">
      <img src="/lyripass.svg" alt="Lyripass icon" />
      <h1 class="brand-wordmark">lyri<span>pass</span></h1>
      <p>Every word, in time.</p>
      <div class="glass-panel p-4">
        <span class="studio-kicker">BUILT ON LRCGET</span>
        <p>
          Lyripass is a redesigned fork of LRCGET by Thang Tran and contributors, using LRCLIB for
          lyrics. The interface draws inspiration from Dustalexw’s desktop software.
        </p>
      </div>
      <p>
        Browse your collection, download synced lyrics, fine-tune word timings, and export lyrics to
        your music files.
      </p>
      <a
        class="link"
        href="https://github.com/tranxuanthang/lrcget"
        target="_blank"
        rel="noreferrer"
        >LRCGET source and credits ↗</a
      ><a class="link" href="https://lrclib.net" target="_blank" rel="noreferrer">LRCLIB ↗</a>
      <p class="text-xs">Lyripass 0.1 · Based on LRCGET 2.2.1 · MIT license</p>
    </div></BaseModal
  >
</template>
<script setup>
import BaseModal from '@/components/common/BaseModal.vue'
defineEmits(['close'])
</script>
