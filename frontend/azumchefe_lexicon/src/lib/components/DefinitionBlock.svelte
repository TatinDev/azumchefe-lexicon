<script lang="ts">
	import type { Definition } from '$lib/types';

	let { def, numbered = false }: { def: Definition; numbered?: boolean } = $props();
</script>

<li class="text-sm leading-relaxed text-stone-700 {numbered ? 'ml-4 list-decimal' : ''}">
	<p>{def.definition}</p>
</li>
