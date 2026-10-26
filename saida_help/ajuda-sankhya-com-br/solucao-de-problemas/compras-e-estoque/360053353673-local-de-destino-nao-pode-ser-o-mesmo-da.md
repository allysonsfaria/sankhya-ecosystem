---
id: "360053353673"
titulo: "Local de Destino não pode ser o mesmo da Origem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053353673-Local-de-Destino-n%C3%A3o-pode-ser-o-mesmo-da-Origem"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:29:07Z"
rotulos: ["Configuração", "TOP", "Estoque", "CORE_E00775", "Tipo de Operação (TOP)", "Notas de Transferência", "Empresas e Locais", "Erro"]
---

# Local de Destino não pode ser o mesmo da Origem

**Mensagem:**

[CORE\_E00775] Local de Destino não pode ser o mesmo da Origem.

**Causa:**

Ao lançar notas de transferência no sistema, utilizando Tipo de Operação definido com o Tipo de Movimento = T-Transferência, se informado Local = Local destino, para notas de transferência entre locais, a mensagem será apresentada.

**Solução:**

Ao lançar notas de transferência no sistema, utilizando Tipo de Operação definido com o Tipo de Movimento = T-Transferência, avaliar qual processo deseja executar:

**![Imagem 1: Transferência entre EMPRESAS:](https://ajuda.sankhya.com.br/hc/article_attachments/15916292121623)Transferência entre EMPRESAS:**

Nesse caso, ao preencher o cabeçalho da nota, os campos "Empresa" e "Empresa de negociação" **precisam ser diferentes** um do outro (TGFCAB.CODEMP<> TGFCAB.CODEMPNEGOC):

- EMPRESA = Origem
- EMPRESA DE NEGOCIAÇÃO = Destino

![Imagem 2: EMPRESA DE NEGOCIAÇÃO = Destino](https://ajuda.sankhya.com.br/hc/article_attachments/15916307437591)

Para transferência entre empresas, respeitando os critérios acima, será permitido um único local para itens controlados por local (local = local destino) e a validação tratada nesse artigo não ocorrerá;

**![Imagem 3: Transferência entre LOCAIS:](https://ajuda.sankhya.com.br/hc/article_attachments/15916338985879) Transferência entre LOCAIS:**

Para transferência entre LOCAIS (Campo EMPRESA = EMPRESA de negociação), para os itens a serem transferidos de local, o campo **'Local'**deve ser **diferente do campo 'Local Destino'.**

- LOCAL: Local ORIGEM
- LOCAL DESTINO: Local de destino do item

![Imagem 4: LOCAL DESTINO: Local de destino do item](https://ajuda.sankhya.com.br/hc/article_attachments/15916298207895)

**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/15916338990487) Importante:**

- Os campos de 'Local' só serão habilitados se a marcação **"Usa Local"** da aba 'Medidas e Estoque' estiver habilitado. (Marcação a ser realizada conforme processo da empresa, importante sintonia com o implantador responsável).
- Processo de emissão de notas de remessa não deve utilizar TOP de transferência.
