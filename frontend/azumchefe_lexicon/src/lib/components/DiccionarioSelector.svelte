<script lang="ts">
	import type { DictionarySummary } from '$lib/types';
	import DictionaryCard from './DictionaryCard.svelte';

	let {
		diccionarios,
		onselect,
		busqueda = ''
	}: {
		diccionarios: DictionarySummary[];
		onselect: (id: string) => void;
		busqueda?: string;
	} = $props();
</script>

{#if diccionarios.length === 0}
	<div class="py-16 text-center">
		<p class="text-sm text-stone-400">
			{busqueda
				? 'No se encontraron diccionarios con ese nombre'
				: 'No hay diccionarios disponibles'}
		</p>
	</div>
{:else}
	<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
		{#each diccionarios as d (d.id)}
			<DictionaryCard diccionario={d} {onselect} />
		{/each}
	</div>
{/if}
