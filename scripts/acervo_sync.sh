#!/usr/bin/env bash
# Sincroniza o acervo de texto integral (repositório PRIVADO aureliosaraiva/orixas-fontes).
#   scripts/acervo_sync.sh pull   início da sessão: clona ou atualiza em $ACERVO_DIR
#   scripts/acervo_sync.sh push   fim da sessão: commit + push dos arquivos novos na main
# ACERVO_DIR padrão: ../orixas-fontes (irmão deste repositório).
# Nada do acervo entra no repositório público mapadosorixas.
# Em sessão na nuvem, o repositório precisa estar anexado (ferramenta add_repo,
# access push) antes do clone.
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
DIR="${ACERVO_DIR:-$RAIZ/../orixas-fontes}"
URL="${ACERVO_URL:-https://github.com/aureliosaraiva/orixas-fontes.git}"
modo="${1:-pull}"

case "$modo" in
  pull)
    if [ -d "$DIR/.git" ]; then
      git -C "$DIR" pull --rebase origin main
    else
      git clone "$URL" "$DIR"
    fi
    echo "acervo em $(cd "$DIR" && pwd): $(ls "$DIR/txt" 2>/dev/null | wc -l) textos"
    ;;
  push)
    [ -d "$DIR/.git" ] || { echo "sem clone em $DIR (rode: $0 pull)"; exit 1; }
    git -C "$DIR" add -A pdf txt indice.json INDICE.md 2>/dev/null || true
    if git -C "$DIR" diff --cached --quiet; then
      echo "acervo sem mudanças"; exit 0
    fi
    n=$(git -C "$DIR" diff --cached --name-only | wc -l)
    git -C "$DIR" commit -q -m "acervo: ${n} arquivo(s) novos/atualizados ($(date +%F))"
    git -C "$DIR" pull --rebase origin main
    for t in 2 4 8 16; do git -C "$DIR" push -u origin main && break; sleep "$t"; done
    ;;
  *) echo "uso: $0 pull|push"; exit 2 ;;
esac
