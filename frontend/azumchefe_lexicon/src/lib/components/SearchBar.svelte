<script lang="ts">
	let { value = $bindable(), placeholder = 'Buscar...' }: { value?: string; placeholder?: string } =
		$props();
</script>

<div class="relative mb-6">
	<svg
		class="pointer-events-none absolute top-1/2 left-3 size-4 -translate-y-1/2 text-stone-400"
		fill="none"
		stroke="currentColor"
		viewBox="0 0 24 24"
	>
		<path
			stroke-linecap="round"
			stroke-linejoin="round"
			stroke-width="2"
			d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
		/>
	</svg>
	<input
		type="search"
		bind:value
		{placeholder}
		class="w-full rounded-xl border border-stone-200 bg-white py-2.5 pr-4 pl-10 text-sm text-stone-700 outline-none placeholder:text-stone-400 focus:border-stone-400 focus:ring-2 focus:ring-stone-100"
	/>
</div>
