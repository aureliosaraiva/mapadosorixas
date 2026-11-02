// Folha de estilo Cytoscape comum ao Mapa de conexões e ao desenho da página de cada
// orixá. As cores de texto e fundo vêm das variáveis CSS do tema (claro ou escuro);
// chame de novo depois do evento 'tema-mudou' para redesenhar com o tema novo.
export function coresDoTema() {
  const css = getComputedStyle(document.documentElement);
  const v = (n: string, padrao: string) => css.getPropertyValue(n).trim() || padrao;
  return { texto: v('--grafo-texto', '#1f1d1a'), fundo: v('--grafo-fundo', '#fffdf9'), foco: v('--foco', '#1a5fd0'), ocre: v('--ocre', '#8c4c0c') };
}

export function estiloCytoscape(): any[] {
  const c = coresDoTema();
  return [
    { selector: 'node', style: {
      'background-color': 'data(cor)', shape: 'data(forma)', label: 'data(label)',
      'font-size': 11, 'font-family': 'Inter Variable, Inter, system-ui, sans-serif', color: c.texto,
      'text-valign': 'bottom', 'text-margin-y': 4, 'text-wrap': 'wrap', 'text-max-width': '110px', width: 22, height: 22,
      'text-background-color': c.fundo, 'text-background-opacity': 0.85, 'text-background-padding': '2px', 'text-background-shape': 'roundrectangle',
    } },
    { selector: 'node[tipo = "orixa"]', style: { width: 40, height: 40, 'font-size': 14, 'font-weight': 'bold' } },
    { selector: 'node[href != ""]', style: { 'border-width': 3, 'border-color': '#e0b24a' } },
    { selector: 'edge', style: {
      width: 2, 'line-color': 'data(cor)', 'line-style': 'data(estilo)',
      'target-arrow-shape': 'data(seta)', 'target-arrow-color': 'data(cor)', 'curve-style': 'bezier', opacity: 0.85,
    } },
    { selector: '.oculto', style: { display: 'none' } },
    { selector: '.realce', style: { 'border-width': 4, 'border-color': c.foco } },
  ];
}
