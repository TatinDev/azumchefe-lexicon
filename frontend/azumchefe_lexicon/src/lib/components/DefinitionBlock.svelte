<script lang="ts">
	import type { Definition } from '$lib/types';

	let { def, numbered = false }: { def: Definition; numbered?: boolean } = $props();
</script>

<li class="text-sm leading-relaxed text-stone-700 {numbered ? 'ml-4 list-decimal' : ''}">
	<p>{def.text}</p>
	{#if def.editorialNote}
		<p class="mt-0.5 text-xs italic text-stone-500">{def.editorialNote}</p>
	{/if}
	{#if def.quotes && def.quotes.length > 0}
		<div class="mt-1.5 space-y-1 border-l-2 border-stone-200 pl-3">
			{#each def.quotes as q (q.text + (q.targetLanguageText ?? ''))}
				<div>
					<p class="text-sm italic text-stone-600">{q.text}</p>
					{#if q.targetLanguageText}
						<p class="text-xs text-stone-400">— {q.targetLanguageText}</p>
					{/if}
				</div>
			{/each}
		</div>
	{/if}
</li>
