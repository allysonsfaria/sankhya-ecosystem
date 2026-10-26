---
id: "24309550455575"
titulo: "Nota que participa de pacote de remessa tem que ser cancelada, não pode ser excluída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24309550455575-Nota-que-participa-de-pacote-de-remessa-tem-que-ser-cancelada-n%C3%A3o-pode-ser-exclu%C3%ADda"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-10-02T14:14:53Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "TOP", "CORE_E04192", "Nota de remessa não pode ser excluída", "Cancelar a Nota Principal primeiro", "Campo NUREM preenchido na remessa", "Erro"]
---

# Nota que participa de pacote de remessa tem que ser cancelada, não pode ser excluída

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24309550446487) **MENSAGEM:**

[CORE\_E04192] Nota que participa de pacote de remessa tem que ser cancelada, não pode ser excluída

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24309541552151) **SOLUÇÃO:**

Não é permitido **"Cancelar"** diretamente a Nota de Remessa. Para isso, é **preciso primeiro cancelar/excluir a Nota/pedido de Venda ou Compra (Nota Principal) que gerou a Remessa e, então, serão canceladas as duas notas: a Nota Principal e também a de Remessa.** As Notas de Remessa são identificadas pelo campo "Número Remessa" (NUREM) preenchido no Cabeçalho da Nota (TGFCAB). A Nota Principal, que é a que poderá ser excluída/cancelada, é reconhecida pelo campo Tipo de operação remessa no cadastro da top.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24309550454167) **CAUSA:**

O erro é apresentado ao tentar excluir/cancelar uma nota de remessa que tenha o campo NUREM da tgfcab preenchido.
