---
id: "37099263635991"
titulo: "1072 Rejeição: DFe/Item referenciado em duplicidade [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099263635991-1072-Rejei%C3%A7%C3%A3o-DFe-Item-referenciado-em-duplicidade-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-24T23:06:11Z"
rotulos: ["NF-e", "Portal de Vendas", "XML", "SEFAZ", "Erro", "Artigo atualizado KCS", "DFe/Item referenciado", "DFe/Item referenciado em duplicidade", "DFe foi referenciado mais de uma vez na mesma nota fiscal", "impede a referência duplicada de documentos ou itens em um mesmo DFe", "DFe/Item", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# 1072 Rejeição: DFe/Item referenciado em duplicidade [nItem: 999]

**Mensagem**

[1072] Rejeição: DFe/Item referenciado em duplicidade [nItem: X]

**Situação**

A rejeição ocorre na transmissão da NF-e quando a mesma combinação de **Chave de Acesso + número do item referenciado** aparece mais de uma vez no grupo **DFeReferenciado** da nota. Esse grupo foi criado para as novas regras de IBS/CBS da Reforma Tributária.

Os cenários mais comuns são:

- **Devolução de produto com controle de lote:** o produto entrou em uma única linha na nota de compra do fornecedor, mas no sistema foi recebido em lotes diferentes. Na devolução, é gerada uma linha por lote, e todas referenciam o mesmo item da nota original.
- **Notas complementares ou de ajuste:** a mesma chave de acesso e o mesmo item de origem são informados mais de uma vez.
- **Referências inseridas manualmente em duplicidade** no lançamento da nota.

**Solução**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Primeiramente, verifique se o sistema está atualizado. Recomenda-se utilizar a versão 4.35b502 ou superior do Sankhya e o módulo Livros Fiscais na versão 5.28.0 ou superior, realizando a atualização preferencialmente em base de teste.

**(2)** Para notas de devolução, acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) utilizada na operação.

**(3)** Marque o campo **"Agrupar produtos semelhantes na NF-e?"**. Com isso, as linhas do mesmo produto são consolidadas em uma única linha na NF-e, com uma única referência ao item da nota original.

**Importante:** o agrupamento só acontece quando os itens têm as mesmas características (produto, valor unitário, CFOP e tributação). Se os lotes tiverem valores ou tributações diferentes, as linhas não serão agrupadas e a rejeição pode continuar. Nesse caso, revise os valores dos itens na nota de devolução.

**(4)** Salve a **"Tipos de Operação - TOP"**, retorne à nota fiscal de devolução e gere novamente o documento fiscal.

**(5)** Se a rejeição continuar, ou se a nota não for de devolução, acesse a tela **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas). No **"Botão NF-e"**, use a opção **"Gerar XML da NF-e em arquivo para Conferência"**.

**(6)** Abra o XML e pesquise (Ctrl+F) pela tag **DFeReferenciado**. Verifique se o mesmo par **chaveAcesso + nItem** aparece mais de uma vez. O item indicado na rejeição ([nItem: X]) ajuda a localizar o ponto do erro.

**(7)** Após identificar a duplicidade, acesse o lançamento da nota e remova as referências repetidas. Depois gere e transmita a NF-e novamente.

**Causa**

A rejeição vem de uma validação da SEFAZ que proíbe referenciar o mesmo documento e o mesmo item mais de uma vez em um DFe. O objetivo é garantir a integridade das informações fiscais, principalmente no cálculo e na apuração de IBS/CBS.

As principais causas são:

- Em devoluções, o controle de lotes gera várias linhas para o mesmo produto, e cada uma referencia o mesmo item da nota original.
- A TOP não está configurada para agrupar produtos semelhantes na NF-e.
- O sistema está em uma versão sem o tratamento dessa regra.
- Referências duplicadas foram informadas manualmente no lançamento.
