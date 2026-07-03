import type { DictEntry } from '$lib/types';
import { LANGUAGE_NAMES, POS_NAMES, GEO_MARKS, CONTEXT_MARKS } from '$lib/constants';

export const API_BASE = import.meta.env.VITE_API_BASE ?? '/api';

export function langName(code: string): string {
	return LANGUAGE_NAMES[code] ?? code;
}

export function expandPOS(pos: string | undefined): string[] {
	if (!pos) return [];
	return pos.split(',').map((p) => POS_NAMES[p.trim()] ?? p.trim());
}

export function geoMarkName(mark: string | undefined): string {
	return GEO_MARKS[mark ?? ''] ?? mark ?? '';
}

export function restrictionMarkName(mark: string | undefined): string {
	return CONTEXT_MARKS[mark ?? ''] ?? mark ?? '';
}

export function entrySearchText(e: DictEntry): string {
	const parts: string[] = [e.lemma];
	for (const f of e.forms ?? []) parts.push(f.text);
	for (const s of e.senses) {
		for (const d of s.definitions ?? []) {
			parts.push(d.text);
			for (const q of d.quotes ?? []) {
				parts.push(q.text, q.targetLanguageText ?? '');
			}
		}
		for (const r of s.references ?? []) parts.push(r.text);
	}
	for (const sub of e.sublevelEntries ?? []) parts.push(entrySearchText(sub));
	return parts.join(' ').toLowerCase();
}

export function firstDefinition(e: DictEntry): string {
	for (const s of e.senses) {
		for (const d of s.definitions ?? []) return d.text;
	}
	return '';
}

export function firstPOS(e: DictEntry): string | undefined {
	return e.senses[0]?.partOfSpeech;
}
