---
id: "9221464635415"
titulo: "Não foram encontrados documentos de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga com os modelos de documentos 1, 1A, 4, 8, 55 ou 57"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9221464635415-N%C3%A3o-foram-encontrados-documentos-de-venda-transfer%C3%AAncia-ou-conhecimento-de-transporte-na-s-ordem-ns-de-carga-com-os-modelos-de-documentos-1-1A-4-8-55-ou-57"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:18Z"
rotulos: ["ERROMDFE", "MDF-e", "Fiscal", "SEFAZ", "Transporte", "CORE_E01476", "Erro de Documentos Não Encontrados", "Documentos Eletrônicos"]
---

# Não foram encontrados documentos de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga com os modelos de documentos 1, 1A, 4, 8, 55 ou 57

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/15855833131031) MENSAGEM:**

[CORE\_E01476] Não foram encontrados documentos de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga com os modelos de documentos 1, 1A, 4, 8, 55 ou 57.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15855828011671) CAUSA:**

Poderá ocorrer quando a nota vinculada ao MDF-e não estiver aprovada, notas vinculadas a OC diferente da OC vinculada ao MDF-e ou ainda por não informar a empresa por ordem de carga no caso de trabalhar com mais de uma empresa.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15855828016023) SOLUÇÃO:**

- Para cancelar o MDF-e é necessário que a nota vinculada a ele esteja aprovada;
- Para encerrar o MDF-e verifique em qual OC as notas estão vinculadas, pois o MDF-e precisa estar vinculado na mesma OC.
- Verifique para qual empresa o MDF-e tem OC e confira no cadastro da **Empresa** (Caminho de acesso à tela: Comercial » Preferências » Empresa) qual a empresa informada.

![Imagem 4: Verifique para qual empresa o MDF-e tem OC e confira no cadastro da Empresa (Caminho de acesso à tela: Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/15855842955927)

**Exemplo:**

- Se a Empresa 2 é responsável por suas próprias Ordens de Carga , mantenha o campo Empresas p/ Ordem de Carga EM BRANCO;
- Caso as Ordens de Carga sejam concentradas na empresa 2, informe no campo Empresas p/ Ordem de Carga das DEMAIS empresa o código da empresa 2.

O campo **"Empresa por Ordem de Carga"** permitirá o lançamento de vários pedidos para empresas diferentes, realizando o transporte por apenas uma empresa.

Assim, na tela [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274) será possível vincular a ordem de carga da empresa transportadora em pedidos lançados para outras empresas, ou seja, será considerada a ordem de carga da empresa inserida neste campo.
