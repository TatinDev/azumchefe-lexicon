<script lang="ts">
	import type { Sense } from '$lib/types';
	import SenseBadges from './SenseBadges.svelte';
	import DefinitionBlock from './DefinitionBlock.svelte';

	let {
		sense,
		index,
		onnavigate
	}: { sense: Sense; index: number; onnavigate: (lemma: string) => void } = $props();
</script>

<div class="mb-5 {index > 0 ? 'border-t border-stone-100 pt-4' : ''}">
	<SenseBadges {sense} />

	{#if sense.editorialNote}
		<p class="mb-2 text-xs italic text-stone-500">{sense.editorialNote}</p>
	{/if}

	{#if sense.definitions && sense.definitions.length > 0}
		<ol class="space-y-2">
			{#each sense.definitions as def, di (di)}
				<DefinitionBlock {def} numbered={sense.definitions!.length > 1} />
			{/each}
		</ol>
	{/if}

	{#if sense.references && sense.references.length > 0}
		<div class="flex flex-wrap gap-2">
			{#each sense.references as ref (ref.text)}
				<button
					type="button"
					onclick={() => onnavigate(ref.text)}
					class="cursor-pointer rounded-lg bg-stone-50 px-3 py-1.5 text-sm text-stone-600 transition-colors hover:bg-stone-100 hover:text-stone-800"
				>
					→ {ref.text}
				</button>
			{/each}
		</div>
	{/if}
</div>
