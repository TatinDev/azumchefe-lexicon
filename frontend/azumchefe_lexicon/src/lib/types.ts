export interface Quote {
	text: string;
	targetLanguageText?: string;
}

export interface Definition {
	text: string;
	quotes?: Quote[];
	editorialNote?: string;
}

export interface Reference {
	text: string;
	isExternal?: string;
	editorialNote?: string;
}

export interface Sense {
	partOfSpeech?: string;
	geographicalMark?: string;
	restrictionMark?: string;
	editorialNote?: string;
	definitions?: Definition[];
	references?: Reference[];
}

export interface Form {
	text: string;
	doNotIndex?: string;
	editorialNote?: string;
}

export interface DictEntry {
	lemma: string;
	forms?: Form[];
	senses: Sense[];
	sublevelEntries?: DictEntry[];
}

export interface Dictionary {
	id: string;
	label: string;
	sourceLanguage: string;
	targetLanguage: string;
	entries: DictEntry[];
}

export interface DictionarySummary {
	id: string;
	label: string;
	sourceLanguage: string;
	targetLanguage: string;
	entryCount: number;
}
