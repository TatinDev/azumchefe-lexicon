<script lang="ts">
	import type { Dictionary } from '$lib/types';
	import { langName, API_BASE } from '$lib/helpers';

	let {
		diccionario,
		diccionarioId,
		entryCount,
		onback
	}: {
		diccionario: Dictionary | null;
		diccionarioId: string;
		entryCount: number;
		onback: () => void;
	} = $props();

	let downloadUrl = $derived(`${API_BASE}/dictionaries/${diccionarioId}?download=true`);
</script>

<div class="mb-4 flex items-center gap-3">
	<button
		type="button"
		onclick={onback}
		class="flex size-8 shrink-0 items-center justify-center rounded-lg text-stone-400 transition-colors hover:bg-stone-100 hover:text-stone-600"
		aria-label="Volver"
	>
		<svg class="size-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="1.5"
				d="M15.75 19.5 8.25 12l7.5-7.5"
			/>
		</svg>
	</button>
	<div class="min-w-0">
		<h2 class="truncate text-lg font-medium text-stone-800">
			{diccionario?.label ?? ''}
		</h2>
		<p class="truncate text-xs text-stone-500">
			{diccionario
				? `${langName(diccionario.sourceLanguage)} → ${langName(diccionario.targetLanguage)}`
				: ''}
		</p>
	</div>
	<button
		type="button"
		onclick={() => window.open(downloadUrl, '_blank')}
		class="ml-auto flex size-7 shrink-0 items-center justify-center rounded-lg text-stone-400 transition-colors hover:bg-stone-100 hover:text-stone-600"
		aria-label="Descargar JSON"
		title="Descargar JSON"
	>
		<svg class="size-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3"
			/>
		</svg>
	</button>
	<span class="shrink-0 rounded-full bg-stone-100 px-3 py-1 text-xs text-stone-500">
		{entryCount} entradas
	</span>
</div>
