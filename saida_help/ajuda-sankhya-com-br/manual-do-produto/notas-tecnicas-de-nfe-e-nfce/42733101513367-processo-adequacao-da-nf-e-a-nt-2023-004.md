---
id: "42733101513367"
titulo: "Processo Adequação da NF-e à NT 2023.004 v.1.11"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42733101513367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2023-004-v-1-11"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2023.004 v.1.11

**Caminhos de Acesso:** Menu Principal › Preferências › Empresa › aba NF-e/NFC-e › sub-aba Nota Técnica NF-e

---

## O que é e para que serve

A Nota Técnica 2023.004 - v.1.11 divulga novos campos e regras de validação da NF-e versão 1.11. Foram criados novos campos no grupo YA - Informações de Pagamento e nos grupos de Tributação do ICMS com ICMS desonerado, além de alterações nos Grupos I01 (Produtos e Serviços / Declaração de Importação) e Z (Informações Adicionais da NF-e).

## O que foi alterado e Configurações

Para utilizar esta Nota Técnica, acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNF-e/NFC-e) > Nota Técnica NF-e, e ative a **"Nota Técnica 2023.004 - v.1.11"**. A seguir, confira as gerações das principais tags:

- **Geração da tag <CPF>/<CNPJ> no grupo I01:** Ao registrar uma Nota de Nacionalização, informe o "CNPJ/CPF do Adquirente" na opção Declaração de Importação e Adições para que a respectiva tag seja preenchida corretamente (14 posições para CNPJ ou 11 para CPF).
- **Geração da tag <cAut> e <CNPJ> no grupo YA04:** A partir de 01/07/2024, recebimentos via PIX (API ou TEF) validam o CNPJ da instituição e a autorização da transação. É necessário configurar um Tipo de Título com subtipo PIX (API ou TEF) e vincular à Parceiro Administradora correta para a geração dos dados correspondentes.
- **Geração da tag <indDeduzDeson> nos grupos de Tributação ICMS:** Indica se o valor do ICMS desonerado deduz do valor do item. É preenchida automaticamente conforme a configuração do campo "Indicador Repasse Desoneração" na grade de Itens ou na tela de [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934).
