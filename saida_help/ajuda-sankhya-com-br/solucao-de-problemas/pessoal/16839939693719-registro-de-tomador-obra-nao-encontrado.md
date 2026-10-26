---
id: "16839939693719"
titulo: "Registro de tomador/obra não encontrado para a empresa indicada. Código de recolhimento exige tomador/obra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16839939693719-Registro-de-tomador-obra-n%C3%A3o-encontrado-para-a-empresa-indicada-C%C3%B3digo-de-recolhimento-exige-tomador-obra"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:17:54Z"
rotulos: ["Configuração", "Parceiro", "Folha", "SEFIP", "Erro na Geração do SEFIP", "FGTS", "Erro"]
---

# Registro de tomador/obra não encontrado para a empresa indicada. Código de recolhimento exige tomador/obra

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16839923232791) MENSAGEM:**

Registro de tomador/obra não encontrado para a empresa indicada. Código de recolhimento exige tomador/obra.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16839951488023) SOLUÇÃO:**

**Nota:** **A geração do arquivo SEFIP - Sistema Empresa de Recolhimento do FGTS e Informações à Previdência Social é realizada para trazer as informações da folha calculada do sistema para o aplicativo Sefip da Caixa. Além de ter a possibilidade de integrar com o financeiro apenas os devidos valores relativos ao FGTS da folha.**
Verifique o parâmetro  **"Onde Utiliza o Registro Fiscal - FPREGFISCAL"** se ele é por Empresa ou por Departamento.
Se for por Departamento ele vai exigir uma configuração específica para Sefip devido ao processo de Parceiro Tomador de Obra, onde é configurado o registro fiscal vinculado ao Departamento e todos os funcionários devem estar com o Departamento correto na aba lotação do cadastro, 
 **Se for empresa e mesmo assim ainda esta apresentando o erro, verifique o layout da SEFIP.**

Se o leiaute selecionado estiver incorreto, vai ocasionar também essa mensagem de erro.

Após realizada a importação do leiaute, sua base estará pronta para que o arquivo SEFIP seja emitido. Dessa forma, acesse a tela Geração de Guias, em seguida, acione o menu **"SEFIP"** e **"Geração da Guia"**, respectivamente.
