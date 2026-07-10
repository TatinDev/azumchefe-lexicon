export interface Example {
	example: string;
}

export interface Definition {
	definition: string;
}

export interface Sense {
	partOfSpeech?: string;
	definitions?: Definition[];
	examples?: Example[];
}

export interface DictEntry {
	writtenForm: string;
	variants?: string[];
	senses: Sense[];
}

export interface Dictionary {
	id: string;
	languageIndex: string;
	languageContent: string;
	entries: DictEntry[];
}

export interface DictionarySummary {
	id: string;
	languageIndex: string;
	languageContent: string;
	entryCount: number;
}
