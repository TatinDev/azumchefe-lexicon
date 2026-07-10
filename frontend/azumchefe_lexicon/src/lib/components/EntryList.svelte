<script lang="ts">
	import type { DictEntry } from '$lib/types';
	import EntryListItem from './EntryListItem.svelte';

	let {
		entries,
		selected,
		onselect,
		show = true
	}: {
		entries: DictEntry[];
		selected: DictEntry | null;
		onselect: (e: DictEntry) => void;
		show?: boolean;
	} = $props();
</script>

<div class="w-full space-y-1.5 sm:w-80 sm:shrink-0 {show ? 'block' : 'hidden sm:block'}">
	{#if entries.length === 0}
		<div class="py-12 text-center text-sm text-stone-400">No se encontraron entradas</div>
	{:else}
		<div class="overflow-y-auto sm:max-h-[calc(100dvh-18rem)]">
			{#each entries as e, i (e.writtenForm + '_' + i)}
				<EntryListItem entry={e} selected={selected === e} {onselect} />
			{/each}
		</div>
	{/if}
</div>
