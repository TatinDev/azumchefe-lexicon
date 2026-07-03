<script lang="ts">
	import type { DictEntry } from '$lib/types';
	import SenseBlock from './SenseBlock.svelte';

	let { subentries, onnavigate }: { subentries: DictEntry[]; onnavigate: (lemma: string) => void } =
		$props();
</script>

<div class="border-t border-stone-200 pt-4">
	<h4 class="mb-3 text-xs font-medium uppercase tracking-wider text-stone-400">Subentradas</h4>
	<div class="space-y-4">
		{#each subentries as sub (sub.lemma)}
			<div class="rounded-lg bg-stone-50 p-4">
				<h5 class="text-base font-medium text-stone-800">{sub.lemma}</h5>
				{#if sub.forms && sub.forms.length > 0}
					<p class="text-xs text-stone-400">
						también: {sub.forms.map((f) => f.text).join(', ')}
					</p>
				{/if}
				{#each sub.senses as sense, si (si)}
					<div class="mt-2">
						<SenseBlock {sense} index={si} {onnavigate} />
					</div>
				{/each}
			</div>
		{/each}
	</div>
</div>
