// Folha de estilo Cytoscape comum à página Grafo e ao mini-grafo das fichas.
export const estiloCytoscape: any[] = [
  { selector: 'node', style: {
    'background-color': 'data(cor)', shape: 'data(forma)', label: 'data(label)',
    'font-size': 11, color: '#1f1a17', 'text-valign': 'bottom', 'text-margin-y': 4,
    'text-wrap': 'wrap', 'text-max-width': '110px', width: 22, height: 22,
    'text-background-color': '#ffffff', 'text-background-opacity': 0.8, 'text-background-padding': '1px',
  } },
  { selector: 'node[tipo = "orixa"]', style: { width: 40, height: 40, 'font-size': 14, 'font-weight': 'bold' } },
  { selector: 'node[href != ""]', style: { 'border-width': 3, 'border-color': '#f2c14e' } },
  { selector: 'edge', style: {
    width: 2, 'line-color': 'data(cor)', 'line-style': 'data(estilo)',
    'target-arrow-shape': 'data(seta)', 'target-arrow-color': 'data(cor)', 'curve-style': 'bezier',
  } },
  { selector: '.oculto', style: { display: 'none' } },
  { selector: '.realce', style: { 'border-width': 4, 'border-color': '#0b5cad' } },
];
