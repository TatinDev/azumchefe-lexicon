import type { DictEntry } from '$lib/types';
import { LANGUAGE_NAMES } from '$lib/constants';

export const API_BASE = import.meta.env.VITE_API_BASE ?? '/api';

export function langName(code: string): string {
	return LANGUAGE_NAMES[code] ?? code;
}

export function expandPOS(pos: string | undefined): string[] {
	if (!pos) return [];
	return pos.split(',').map((p) => p.trim());
}

export function entrySearchText(e: DictEntry): string {
	const parts: string[] = [e.writtenForm];
	for (const v of e.variants ?? []) parts.push(v);
	for (const s of e.senses) {
		for (const d of s.definitions ?? []) {
			parts.push(d.definition);
		}
		for (const ex of s.examples ?? []) {
			parts.push(ex.example);
		}
	}
	return parts.join(' ').toLowerCase();
}

export function firstDefinition(e: DictEntry): string {
	for (const s of e.senses) {
		for (const d of s.definitions ?? []) return d.definition;
	}
	return '';
}

export function firstPOS(e: DictEntry): string | undefined {
	return e.senses[0]?.partOfSpeech;
}
