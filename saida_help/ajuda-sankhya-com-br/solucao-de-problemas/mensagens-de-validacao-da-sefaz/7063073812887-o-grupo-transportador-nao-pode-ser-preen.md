---
id: "7063073812887"
titulo: "O Grupo Transportador não pode ser preenchido para Modalidade do frete informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7063073812887-O-Grupo-Transportador-n%C3%A3o-pode-ser-preenchido-para-Modalidade-do-frete-informada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-17T13:41:47Z"
rotulos: ["NF-e", "SEFAZ", "Transporte", "845", "Grupo Transportador Incorreto", "Erro", "Documentos Eletrônicos"]
---

# O Grupo Transportador não pode ser preenchido para Modalidade do frete informada

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16480843385495) MENSAGEM**:

845 - Rejeição: O Grupo Transportador não pode ser preenchido para Modalidade do frete informada.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16480866991767) CAUSA:**

Isso indica que o documento foi emitido com modalidade do frete = 9 (sem ocorrência de transporte), mas foi informado o Grupo transportador.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16480843390615) SOLUÇÃO:**

Se Modalidade do Frete = 9 (id: X02, campo: modFrete), o Grupo Transportador não pode ser informado.

A Ordem de Carga faz com que o Grupo Transportador seja gerado no XM. Se a operação não possui frete, a Ordem de Carga não poderá ser informada.

![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16480866998167) **OBSERVAÇÃO:**

Ao informar a modalidade 9 (sem ocorrência de transporte) entende-se que não haverá o transporte desta mercadoria, sendo assim não deverá conter uma ordem de carga.
Caso a nota em questão tenha necessidade de manter a Ordem de Carga informada no cabeçalho da nota, acesse a tela **"Ordens de Carga"**, localize a ordem de carga informada e altere o Parceiro da OC para o Parceiro '0'

Modalidades de Frete:

0 - Contratação do Frete por conta do Remetente (CIF);
1 - Contratação do Frete por conta do Destinatário(FOB);
2 - Contratação do Frete por conta de Terceiros;
3 - Transporte Próprio por conta do Remetente;
4 - Transporte Próprio por conta do Destinatário;
9 - Sem Ocorrência de Transporte.
