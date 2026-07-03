<script lang="ts">
	import type { Sense } from '$lib/types';
	import { expandPOS, geoMarkName, restrictionMarkName } from '$lib/helpers';

	let { sense }: { sense: Sense } = $props();
</script>

<div class="mb-2 flex flex-wrap items-center gap-1.5">
	{#each expandPOS(sense.partOfSpeech) as pos (pos)}
		<span class="rounded-full bg-stone-100 px-2.5 py-0.5 text-xs text-stone-600">
			{pos}
		</span>
	{/each}
	{#if sense.geographicalMark}
		<span class="rounded-full bg-sky-50 px-2.5 py-0.5 text-xs text-sky-700">
			{geoMarkName(sense.geographicalMark)}
		</span>
	{/if}
	{#if sense.restrictionMark}
		<span class="rounded-full bg-amber-50 px-2.5 py-0.5 text-xs text-amber-700">
			{restrictionMarkName(sense.restrictionMark)}
		</span>
	{/if}
</div>
