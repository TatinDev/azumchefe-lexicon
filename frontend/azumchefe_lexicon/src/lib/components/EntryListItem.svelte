<script lang="ts">
	import type { DictEntry } from '$lib/types';
	import { expandPOS, firstDefinition, firstPOS } from '$lib/helpers';

	let {
		entry,
		selected,
		onselect
	}: { entry: DictEntry; selected: boolean; onselect: (e: DictEntry) => void } = $props();
</script>

<button
	type="button"
	onclick={() => onselect(entry)}
	class="w-full cursor-pointer rounded-lg px-3 py-2.5 text-left text-sm transition-colors {selected
		? 'bg-stone-100'
		: 'hover:bg-stone-50'}"
>
	<span class="font-medium text-stone-800">{entry.writtenForm}</span>
	{#if entry.variants?.[0]}
		<span class="ml-1 text-xs text-stone-400">({entry.variants[0]})</span>
	{/if}
	{#if firstPOS(entry)}
		<span class="ml-2 rounded bg-stone-100 px-1.5 py-0.5 text-xs text-stone-500">
			{expandPOS(firstPOS(entry))[0]}
		</span>
	{/if}
	{#if firstDefinition(entry)}
		<p class="mt-0.5 line-clamp-2 text-xs leading-snug text-stone-400">
			{firstDefinition(entry)}
		</p>
	{/if}
</button>
