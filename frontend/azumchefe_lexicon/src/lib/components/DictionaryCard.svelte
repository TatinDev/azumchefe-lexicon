<script lang="ts">
	import type { DictionarySummary } from '$lib/types';
	import { langName } from '$lib/helpers';

	let {
		diccionario,
		onselect
	}: { diccionario: DictionarySummary; onselect: (id: string) => void } = $props();
</script>

<button
	type="button"
	onclick={() => onselect(diccionario.id)}
	class="group cursor-pointer rounded-xl border border-stone-200 bg-white p-5 text-left shadow-xs transition-all hover:-translate-y-0.5 hover:border-stone-300 hover:shadow-md"
>
	<h3 class="text-lg font-medium text-stone-800">{diccionario.label}</h3>
	<p class="mt-1 text-sm leading-snug text-stone-500">
		{langName(diccionario.sourceLanguage)} → {langName(diccionario.targetLanguage)}
	</p>
	<span class="mt-3 inline-block rounded-full bg-stone-100 px-3 py-1 text-xs text-stone-500">
		{diccionario.entryCount} entradas
	</span>
</button>
