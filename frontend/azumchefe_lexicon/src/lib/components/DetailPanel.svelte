<script lang="ts">
	import type { DictEntry } from '$lib/types';
	import SenseBlock from './SenseBlock.svelte';
	import SubentriesSection from './SubentriesSection.svelte';

	let {
		entry,
		show,
		onnavigate,
		onback
	}: {
		entry: DictEntry | null;
		show: boolean;
		onnavigate: (lemma: string) => void;
		onback: () => void;
	} = $props();
</script>

<div class="flex-1 {show ? 'block' : 'hidden sm:block'}">
	{#if entry}
		<button
			type="button"
			onclick={onback}
			class="mb-3 flex items-center gap-1 text-sm text-stone-500 hover:text-stone-700 sm:hidden"
		>
			<svg class="size-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M15.75 19.5 8.25 12l7.5-7.5"
				/>
			</svg>
			Volver a la lista
		</button>

		<div class="rounded-xl border border-stone-200 bg-white p-6">
			<div class="mb-5 flex items-start justify-between gap-4">
				<div>
					<h3 class="text-2xl font-semibold text-stone-800">{entry.lemma}</h3>
					{#if entry.forms && entry.forms.length > 0}
						<p class="mt-0.5 text-sm text-stone-400">
							también: {entry.forms.map((f) => f.text).join(', ')}
						</p>
					{/if}
				</div>
			</div>

			{#each entry.senses as sense, si (si)}
				<SenseBlock {sense} index={si} {onnavigate} />
			{/each}

			{#if entry.sublevelEntries && entry.sublevelEntries.length > 0}
				<SubentriesSection subentries={entry.sublevelEntries} {onnavigate} />
			{/if}
		</div>
	{:else}
		<div class="flex h-full items-center justify-center py-20 sm:py-32">
			<div class="text-center">
				<svg
					class="mx-auto mb-3 size-10 text-stone-300"
					fill="none"
					stroke="currentColor"
					viewBox="0 0 24 24"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="1"
						d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25"
					/>
				</svg>
				<p class="text-sm text-stone-400">Selecciona una entrada para ver su detalle</p>
			</div>
		</div>
	{/if}
</div>
