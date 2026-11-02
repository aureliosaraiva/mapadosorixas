// tempo de leitura (≈ 200 palavras por minuto)
export const minutosLeitura = (palavras) => Math.max(1, Math.round(palavras / 200));
