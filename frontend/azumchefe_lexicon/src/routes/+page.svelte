<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import type { DictionarySummary, Dictionary, DictEntry } from '$lib/types';
	import { API_BASE, entrySearchText, langName } from '$lib/helpers';
	import {
		LoadingSpinner,
		DiccionarioSelector,
		DictionaryHeader,
		SearchBar,
		EntryList,
		DetailPanel
	} from '$lib/components';

	let dictionaries = $state<DictionarySummary[]>([]);
	let searchDictionary = $state('');
	let dictionaryId = $state<string | null>(null);
	let search = $state('');
	let selectedEntry = $state<DictEntry | null>(null);
	let loadingList = $state(true);
	let loadingDictionary = $state(false);
	let error = $state<string | null>(null);
	let showingDetail = $state(false);

	let dictionary = $state<Dictionary | null>(null);

	let filteredDictionaries = $derived(
		searchDictionary
			? dictionaries.filter(
					(d) =>
						d.label.toLowerCase().includes(searchDictionary.toLowerCase()) ||
						langName(d.sourceLanguage).toLowerCase().includes(searchDictionary.toLowerCase()) ||
						langName(d.targetLanguage).toLowerCase().includes(searchDictionary.toLowerCase())
				)
			: dictionaries
	);

	let filteredEntries = $derived(
		search
			? (dictionary?.entries.filter((e) => entrySearchText(e).includes(search.toLowerCase())) ?? [])
			: (dictionary?.entries ?? [])
	);

	onMount(async () => {
		try {
			const res = await fetch(`${API_BASE}/dictionaries`);
			if (!res.ok) throw new Error('Error al cargar los diccionarios');
			dictionaries = await res.json();
		} catch {
			error = 'No se pudieron cargar los diccionarios';
		} finally {
			loadingList = false;
		}
	});

	let abortController: AbortController | null = null;
	let backToListTimer: ReturnType<typeof setTimeout> | undefined;

	onDestroy(() => {
		abortController?.abort();
	});

	function selectDictionary(id: string) {
		abortController?.abort();
		dictionaryId = id;
		loadingDictionary = true;
		selectedEntry = null;
		error = null;
		const controller = new AbortController();
		abortController = controller;

		fetch(`${API_BASE}/dictionaries/${id}`, { signal: controller.signal })
			.then((res) => {
				if (!res.ok) throw new Error('No encontrado');
				return res.json();
			})
			.then((data) => {
				if (dictionaryId === id) {
					dictionary = data;
					loadingDictionary = false;
				}
			})
			.catch((err) => {
				if (err.name === 'AbortError') return;
				if (dictionaryId === id) {
					error = 'Error al cargar el diccionario';
					loadingDictionary = false;
				}
			});
	}

	function selectEntry(e: DictEntry) {
		selectedEntry = e;
		showingDetail = true;
	}

	function backToList() {
		showingDetail = false;
		clearTimeout(backToListTimer);
		backToListTimer = setTimeout(() => {
			selectedEntry = null;
		}, 150);
	}

	function searchAndSelect(headword: string) {
		const entry = dictionary?.entries.find(
			(e) => e.lemma === headword || e.sublevelEntries?.some((s) => s.lemma === headword)
		);
		if (entry) {
			selectedEntry = entry;
			showingDetail = true;
		}
	}

	function backToSelector() {
		dictionaryId = null;
		dictionary = null;
		selectedEntry = null;
	}
</script>

<div class="mx-auto flex min-h-dvh max-w-6xl flex-col px-4 pb-12 pt-6 sm:px-6">
	<header class="mb-8 text-center">
		<h1 class="text-4xl font-light tracking-tight text-stone-800">Azümchefe Lexicon</h1>
		<p class="mt-1 text-sm text-stone-400">Diccionarios mapuche — consulta y explora palabras</p>
	</header>

	{#if loadingList}
		<LoadingSpinner />
	{:else if error && !dictionaryId}
		<div class="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-600">
			{error}
		</div>
	{:else if !dictionaryId}
		<SearchBar bind:value={searchDictionary} placeholder="Buscar diccionario..." />
		<DiccionarioSelector
			diccionarios={filteredDictionaries}
			onselect={selectDictionary}
			busqueda={searchDictionary}
		/>
	{:else}
		<DictionaryHeader
			diccionario={dictionary}
			diccionarioId={dictionaryId}
			entryCount={dictionary?.entries.length ?? 0}
			onback={backToSelector}
		/>
		<SearchBar bind:value={search} />
		{#if loadingDictionary}
			<LoadingSpinner />
		{:else if error}
			<div class="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-600">
				{error}
			</div>
		{:else}
			<div class="flex flex-1 gap-6">
				<EntryList
					entries={filteredEntries}
					selected={selectedEntry}
					onselect={selectEntry}
					show={!showingDetail}
				/>
				<DetailPanel
					entry={selectedEntry}
					show={showingDetail}
					onnavigate={searchAndSelect}
					onback={backToList}
				/>
			</div>
		{/if}
	{/if}
</div>
