// Textos fixos da interface que o scripts/qa_site.py confere (mude os dois juntos).
export const AVISO_REVISAO = 'Conteúdo em revisão por especialistas';
// tempo de leitura (≈ 200 palavras por minuto)
export const minutosLeitura = (palavras) => Math.max(1, Math.round(palavras / 200));
