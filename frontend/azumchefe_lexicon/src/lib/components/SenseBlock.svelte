<script lang="ts">
	import type { Sense } from '$lib/types';
	import SenseBadges from './SenseBadges.svelte';
	import DefinitionBlock from './DefinitionBlock.svelte';

	let { sense, index }: { sense: Sense; index: number } = $props();
</script>

<div class="mb-5 {index > 0 ? 'border-t border-stone-100 pt-4' : ''}">
	<SenseBadges {sense} />

	{#if sense.definitions && sense.definitions.length > 0}
		<ol class="space-y-2">
			{#each sense.definitions as def, di (di)}
				<DefinitionBlock {def} numbered={sense.definitions!.length > 1} />
			{/each}
		</ol>
	{/if}

	{#if sense.examples && sense.examples.length > 0}
		<div class="mt-1.5 space-y-1 border-l-2 border-stone-200 pl-3">
			{#each sense.examples as ex (ex.example)}
				<div>
					<p class="text-sm italic text-stone-600">{ex.example}</p>
				</div>
			{/each}
		</div>
	{/if}
</div>
