---
id: "34108786627607"
titulo: "Propriedade 'ArquivoRelatorio.NOME' com largura acima do limite: (XX > XX)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34108786627607-Propriedade-ArquivoRelatorio-NOME-com-largura-acima-do-limite-XX-XX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:27:44Z"
rotulos: ["Configuração", "Relatórios", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "ArquivoRelatorio.NOME", "nome ultrapassa o limite de caracteres permitido pelo sistema", "largura acima", "limite: (XX XX)", "inserir ou atualizar um relatório no \"Sankhya\"", "utilizando um arquivo \".jrxml\"", "Sankhya"]
---

# Propriedade 'ArquivoRelatorio.NOME' com largura acima do limite: (XX > XX)

**MENSAGEM**

Propriedade 'ArquivoRelatorio.NOME' com largura acima do limite: (XX XX)

**SITUAÇÃO**

O erro ocorre ao tentar inserir ou atualizar um relatório no **"Sankhya"** utilizando um arquivo **".jrxml"** cujo nome ultrapassa o limite de caracteres permitido pelo sistema.

**SOLUÇÃO**

**(1)**  Localize o arquivo **".jrxml"** que está sendo utilizado.

**(2)**  Renomeie o arquivo para que o nome completo (incluindo **".jrxml"**) não ultrapasse o limite informado na mensagem de erro (o sistema exibe **XX > XX**, onde o segundo valor é o tamanho máximo permitido).

**(3)**  Salve o arquivo com o novo nome.

**(4)**  Faça o upload novamente na tela de **"Gerenciamento de Relatórios".**

### **(1)** Dicas:

- Utilize nomes curtos, objetivos e sem espaços desnecessários.
- Caso queira manter uma identificação, use abreviações.

**CAUSA**

O campo **"NOME"** do arquivo de relatório possui um tamanho máximo definido internamente.
Quando o nome do arquivo (incluindo a extensão **".jrxml"**) excede esse limite, o sistema bloqueia a operação e exibe a mensagem de erro.

**Exemplo:**
Nome permitido: **relatorio\_vendas\_2025.jrxml** (29 caracteres)
Nome inválido: **relatorio\_vendas\_detalhado\_por\_regiao\_setor\_financeiro.jrxml** (63 caracteres)

**Causas do erro:**
Nome original do arquivo muito extenso.
Inclusão de informações desnecessárias no nome, como datas, descrições longas ou caracteres redundantes.
